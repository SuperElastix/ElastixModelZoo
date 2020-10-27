#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Copyright (c) University Medical Center Utrecht. All rights reserved.
Created on Mon Mar 19 14:04:25 2012

@author: Floris Berendsen

This script can be used as a command line tool to build a model for the StatisticalShapePenalty elastix module.
Run: "StatisticalShapePenalty.py --help" for the options.
The vtk and numpy libraries are needed. For windows users installing pythonxy is an easy way to get these.
For Python scripting "import StatisticalShapePenalty" provides access to all defined functions.


If you use the StatisticalShapePenalty anywhere we would appreciate if you cite the following article:
F.F. Berendsen et al., Free-form image registration regularized by a statistical shape model: application to organ segmentation in cervical MR, Comput. Vis. Image Understand. (2013), http://dx.doi.org/10.1016/j.cviu.2012.12.006


"""

import vtk, numpy, os.path, sys
from optparse import OptionParser

def readsamples(trainingsettxt, leaveout, logout = sys.stdout):
    trainingfile = open(trainingsettxt,'r')
    vtkfiles=[]
    for trainingline in trainingfile:
        if (trainingline[0]=='#'):  # '#' is used as comment symbol
            logout.write('Skipped: %s' % trainingline)
            continue
        if (not leaveout==None):
            if (leaveout in trainingline):
                logout.write('left patient out: %s' % trainingline)
                continue
        if os.path.getsize(trainingline.rstrip()) < 200:
            logout.write('file size too small: %s' % trainingline)
            continue
        #print(trainingline)
        vtkfiles.append(trainingline.strip())
            
    trainingfile.close()
    polydata, samples = readvtkdata(vtkfiles,logout)
    return polydata, samples, vtkfiles
    
def readvtkdata(vtkfiles,logout = sys.stdout):
    reader=vtk.vtkPolyDataReader()
    samples = None
    numberOfPoints = samplesize_3 = 0
    for k,vtkfile in enumerate(vtkfiles):
        reader.SetFileName(vtkfile)
        polydata = vtk.vtkPolyData()
        reader.Update()
        polydata = reader.GetOutput()
        numberOfPoints = polydata.GetNumberOfPoints()
        #print(numberOfPoints)
        if (samples==None):
            samplesize_3=numberOfPoints
            samples = numpy.zeros((len(vtkfiles),samplesize_3*3))
        elif (not numberOfPoints== samplesize_3):
            logout.write('Number of vertices not matching. Aborting')
            raise ValueError('Number of vertices not matching')
        points = polydata.GetPoints()
        for point_inx in range(polydata.GetNumberOfPoints()):
            coord = points.GetPoint(point_inx)
            samples[k,(point_inx*3):((point_inx+1)*3)]=coord
    #print(samples)
    Nsamples=samples.shape[0]
   # print(Nsamples)
    
    logout.write('\nNumber of 3D-vertices: %d\nNumber of samples: %d'%(numberOfPoints,Nsamples))

    return polydata, samples
    
def shapeToPolydata(polydata,shape):
    SB=shape.squeeze()
    points = polydata.GetPoints()
    for point_inx in range(polydata.GetNumberOfPoints()):
        coord = tuple(SB[(point_inx*3):((point_inx+1)*3)])
        points.SetPoint(point_inx,coord)
    polydata.SetPoints(points)
    polydata.Update()
    return polydata
    
def normalizeSamples(sample):
    # samples must be a 2d numpy array with on the first dimension one or more individuals and on the second dimension the concatenated x-y-z coordinates. samples[patindex,vectorindex]
    numberOfPoints=sample.shape[1]/3
    centroids=numpy.mean(sample.reshape(-1,numberOfPoints,3),axis=1)
    tnormalizedSamples=(sample.reshape(-1,numberOfPoints,3) - centroids.reshape((-1,1,3))).reshape((-1,numberOfPoints*3))

    l2norms=numpy.sqrt((tnormalizedSamples**2).sum(axis=1)/numberOfPoints).reshape(-1,1) # reshape it explicitly into a 2d column vector

    sizeNormalizedSamples = tnormalizedSamples/l2norms

    normalizedsamples=numpy.column_stack((sizeNormalizedSamples,centroids,l2norms)) # create new sample vectors
    return normalizedsamples
def normalizeDerivatives(sample, derivSample):
    if sample.shape[0]>1:
        raise(ValueError('only 1 sample is supported'))
    numberOfPoints=derivSample.shape[1]/3
    centroids=numpy.mean(sample.reshape(-1,numberOfPoints,3),axis=1)
    tnormalizedSamples=(sample.reshape(-1,numberOfPoints,3) - centroids.reshape((-1,1,3))).reshape((-1,numberOfPoints*3))
    l2norms=numpy.sqrt((tnormalizedSamples**2).sum(axis=1)/numberOfPoints).reshape(-1,1) # reshape it explicitly into a 2d column vector
    sizeNormalizedSamples = tnormalizedSamples/l2norms
    normalizedSamples=numpy.column_stack((sizeNormalizedSamples,centroids,l2norms)) # create new sample vectors
    
    derivCentroids=numpy.mean(derivSample.reshape(-1,numberOfPoints,3),axis=1)
    tnormalizedDerivSamples=(derivSample.reshape(-1,numberOfPoints,3) - derivCentroids.reshape((-1,1,3))).reshape((-1,numberOfPoints*3))
    derivL2norms=numpy.sum(tnormalizedSamples*tnormalizedDerivSamples,axis=1).reshape(-1,1)/numberOfPoints/l2norms
    sizeNormalizedDerivSamples = tnormalizedDerivSamples/l2norms - (derivL2norms/l2norms**2) * tnormalizedSamples
    normalizedDerivs=numpy.column_stack((sizeNormalizedDerivSamples,derivCentroids,derivL2norms)) # create new derivative sample vector
    return normalizedSamples, normalizedDerivs
def denormalizeSamples(normalizedSample):

    numberOfPoints=(normalizedSample.shape[1]-4)/3
    l2norms=normalizedSample[:,-1:]
    centroids=normalizedSample[:,-4:-1]
    desample=((normalizedSample[:,:-4]*l2norms).reshape(-1,numberOfPoints,3) + centroids.reshape((-1,1,3))).reshape((-1,numberOfPoints*3))

    return desample

def buildModel(samples):
    #Nsamples=samples.shape[0]
    #numberOfPoints==samples.shape[1]/3
       
    C= numpy.cov(samples,rowvar=0) 
    M=numpy.mean(samples,axis=0)
    D,V = numpy.linalg.eigh(C)
    
    sortinx = D.argsort()
    Dsort=D[sortinx[::-1]]
    Vsort=V[:,sortinx[::-1]]
    
    nonzeros= Dsort>1e-10
    Dpartial = Dsort.compress(nonzeros)
    Vpartial = Vsort.compress(nonzeros,axis=1)
    

    print('Number of non-zero eigenvalues: %d'%numpy.sum(nonzeros))
    model = dict({'M':M , 'Dpartial': Dpartial, 'Vpartial': Vpartial,'C':C})
    return model
def buildNormalizedScaledModel(normalizedSamples,scale):
    #Nsamples=samples.shape[0]
    #numberOfPoints==samples.shape[1]/3
    # The mean of a set of normalized samples not necessarily is a normalized sample itself. 
    M=numpy.mean(normalizedSamples,axis=0)
    
    # In order to get a normalized sample, the arithmetic mean M is denormalized and renormalized again.
    denormM = denormalizeSamples(M.reshape((1,-1)))
    M2= normalizeSamples(denormM).reshape(-1)
    
    C2 = numpy.dot((normalizedSamples-M2).T,normalizedSamples-M2) /(normalizedSamples.shape[0]-1)
    C2scaled=C2/scale.reshape((1,-1))/scale.reshape((-1,1))
    M2scaled=M2/scale
    
    D,V = numpy.linalg.eigh(C2)
    
    sortinx = D.argsort()
    Dsort=D[sortinx[::-1]]
    Vsort=V[:,sortinx[::-1]]
    
    nonzeros= Dsort>1e-10
    Dpartial = Dsort.compress(nonzeros)
    Vpartial = Vsort.compress(nonzeros,axis=1)
    

    print('Number of non-zero eigenvalues: %d'%numpy.sum(nonzeros))
    model = dict({'M':M2scaled , 'Dpartial': Dpartial, 'Vpartial': Vpartial,'C':C2scaled})
    return model    
def buildNormalizedModel(normalizedSamples,reprojectmode=1):
    #Nsamples=samples.shape[0]
    #numberOfPoints==samples.shape[1]/3
    # The mean of a set of normalized samples not necessarily is a normalized sample itself. 
    M=numpy.mean(normalizedSamples,axis=0)
    if reprojectmode==1:
        # In order to get a normalized sample, the arithmetic mean M is denormalized and renormalized again.
        denormM = denormalizeSamples(M.reshape((1,-1)))
        M2= normalizeSamples(denormM).reshape(-1)
    elif reprojectmode==2:
        M2= normalizeSamples(M[:-4].reshape(1,-1)).reshape(-1)
        M2[-4:]=M[-4:]
    
    C2 = numpy.dot((normalizedSamples-M2).T,normalizedSamples-M2) /(normalizedSamples.shape[0]-1)
    
    D,V = numpy.linalg.eigh(C2)
    
    sortinx = D.argsort()
    Dsort=D[sortinx[::-1]]
    Vsort=V[:,sortinx[::-1]]
    
    nonzeros= Dsort>1e-10
    Dpartial = Dsort.compress(nonzeros)
    Vpartial = Vsort.compress(nonzeros,axis=1)
    

    print('Number of non-zero eigenvalues: %d'%numpy.sum(nonzeros))
    model = dict({'M':M2 , 'Dpartial': Dpartial, 'Vpartial': Vpartial,'C':C2})
    return model    

def projectModel(samples,model):
    #numberOfPoints=sample.shape[1]/3
    B= numpy.dot(samples-model['M'],model['Vpartial'])/numpy.sqrt(model['Dpartial'])
    #B=((numpy.asmatrix(model['Vpartial']).T * numpy.asmatrix(samples-model['M']).T).T/numpy.sqrt(model['Dpartial'])).T
    #B: vector(s) with number of standard deviations away from mean, for each modelparameter
    return B

            
def generateSample(model, B):
    sample = model['M']+numpy.dot(B*numpy.sqrt(model['Dpartial']),model['Vpartial'].T)
    return sample


def getIndependentVariances(samples):
    return numpy.var(samples,axis=0,ddof=1)            
 
def getTotalVariance(samples):
    return numpy.sum(getIndependentVariances(samples))/samples.shape[1]

def regularizationScaling(samples,scale):
    return samples/scale.reshape((1,-1))

def regularizationDescale(samples,scale):
    return samples*scale.reshape((1,-1))

def mahalanobis(samples,model,shrinkmix):
    if shrinkmix==0:
        rotatedsample=numpy.dot(samples-model['M'],model['Vpartial'])
        mahal= numpy.sqrt(numpy.sum(rotatedsample**2/model['Dpartial'],axis=1))
    else:
        centeredsample=samples-model['M']
        Dhat=-shrinkmix - (shrinkmix**2/(1.0-shrinkmix)/model['Dpartial'])
        rotatedsample=numpy.dot(centeredsample,model['Vpartial'])
        A=numpy.sum(rotatedsample**2/Dhat,axis=1)
        B=1.0/shrinkmix * numpy.sum(centeredsample**2,axis=1)
        mahal = numpy.sqrt(A+B)
    return mahal

def mahalanobisDerivatives(samples,partDerivs,model,shrinkmix):
    if samples.shape[0]>1:
        raise(ValueError('only 1 sample is supported'))
    if shrinkmix==0:
        rotatedsample=numpy.dot(samples-model['M'],model['Vpartial'])
        mahal= numpy.sqrt(numpy.dot(rotatedsample/model['Dpartial'],rotatedsample.T))
        rotatedDeriv = numpy.dot(partDerivs,model['Vpartial'])
        mahalDeriv = numpy.sum(rotatedsample/model['Dpartial']*rotatedDeriv,axis=1)
    else:
        centeredsample=samples-model['M']
        Dhat=-shrinkmix - (shrinkmix**2/(1.0-shrinkmix)/model['Dpartial'])
        rotatedsample=numpy.dot(centeredsample,model['Vpartial'])
        A=numpy.sum(rotatedsample**2/Dhat,axis=1)
        B=1.0/shrinkmix * numpy.sum(centeredsample**2,axis=1)
        mahal = numpy.sqrt(A+B)
        
        rotatedDeriv = numpy.dot(partDerivs,model['Vpartial'])
        ADeriv=numpy.sum(rotatedsample/Dhat*rotatedDeriv,axis=1)
        BDeriv = 1.0/shrinkmix * numpy.sum(centeredsample*partDerivs,axis=1)
        
        mahalDeriv=(ADeriv + BDeriv)/mahal

    return mahal, mahalDeriv
def buildRegularizedModel(samples,baseVariance,shrinkmix):
    #test function
       
    C= numpy.cov(samples,rowvar=0) 
    C=(1-shrinkmix)*C+shrinkmix*numpy.diag(baseVariance)
    M=numpy.mean(samples,axis=0)
    D,V = numpy.linalg.eigh(C)
    
    sortinx = D.argsort()
    Dsort=D[sortinx[::-1]]
    Vsort=V[:,sortinx[::-1]]
    
    nonzeros= Dsort>1e-10
    Dpartial = Dsort.compress(nonzeros)
    Vpartial = Vsort.compress(nonzeros,axis=1)
    

    print('Number of non-zero eigenvalues: %d'%numpy.sum(nonzeros))
    model = dict({'M':M , 'Dpartial': Dpartial, 'Vpartial': Vpartial,'C':C})
    return model
def buildRegularizedNormalizedModel(normalizedSamples,baseVariance,shrinkmix,reprojectmode=1):
    #test function: regularization is applied in model building, resulting in afull rank matrix
    #To evaluate mahalanobis distance with this model use shrinkmix=0

    # The mean of a set of normalized samples not necessarily is a normalized sample itself. 
    M=numpy.mean(normalizedSamples,axis=0)
    if reprojectmode==1:
        # In order to get a normalized sample, the arithmetic mean M is denormalized and renormalized again.
        denormM = denormalizeSamples(M.reshape((1,-1)))
        M2= normalizeSamples(denormM).reshape(-1)
    elif reprojectmode==2:
        M2= normalizeSamples(M[:-4].reshape(1,-1)).reshape(-1)
        M2[-4:]=M[-4:]
    
    C = numpy.dot((normalizedSamples-M2).T,normalizedSamples-M2) /(normalizedSamples.shape[0]-1)
    
    C=(1-shrinkmix)*C+shrinkmix*numpy.diag(baseVariance)

    D,V = numpy.linalg.eigh(C)
    
    sortinx = D.argsort()
    Dsort=D[sortinx[::-1]]
    Vsort=V[:,sortinx[::-1]]
    
    nonzeros= Dsort>1e-10
    Dpartial = Dsort.compress(nonzeros)
    Vpartial = Vsort.compress(nonzeros,axis=1)
    

    print('Number of non-zero eigenvalues: %d'%numpy.sum(nonzeros))
    model = dict({'M':M2 , 'Dpartial': Dpartial, 'Vpartial': Vpartial,'C':C})
    return model
def mahalanobisBaseVar(samples,model,shrinkmix,baseVar):
    #test function
    if shrinkmix==0:
        rotatedsample=numpy.dot(samples-model['M'],model['Vpartial'])
        mahal= numpy.sqrt(numpy.sum(rotatedsample**2/model['Dpartial'],axis=1))
    else:    
        Dhat= -shrinkmix*baseVar - (((shrinkmix*baseVar)**2)/((1.0-shrinkmix)*model['Dpartial']))
        rotatedsample=numpy.dot(samples-model['M'],model['Vpartial'])
        A=numpy.sum(rotatedsample**2/Dhat,axis=1)
        B=1.0/(shrinkmix*baseVar) * numpy.dot(samples-model['M'],(samples-model['M']).T)
        mahal = numpy.sqrt(A+B)
    return mahal
        


def setupparams():
    usage = "usage: %prog  [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-t", "--trainingset", dest="trainingset", default='trainingset.txt',
                      help="File containing line separated paths to vtk polydata files. '#' is the comment symbol")
    parser.add_option("-n", "--normalize", dest="normalize", default=None,
                      help="")
    parser.add_option("-r", "--reprojectmode", dest="reprojectmode", default=None,
                      help="")                    
    parser.add_option("-m", "--meanout", dest="meanout", default='meanvector.txt', 
                      help="")
    parser.add_option("-p", "--meanvtk", dest="meanvtk", default=None, 
                      help="")
    parser.add_option("-v", "--vectorout", dest="vectorout", default=None,
                      help="")                    
    parser.add_option("-d", "--valueout", dest="valueout", default=None,
                      help="")                      
    parser.add_option("-c", "--covarout", dest="covarout", default="covariance.txt",
                      help="")
    parser.add_option("-l", "--logout", dest="logout", default="buildmodel.log",
                      help="")
    parser.add_option("-o", "--leaveout", dest="leaveout", default=None,
                      help="leave out training sample if string in training file")
    parser.add_option("-e", "--experimental", dest="experimental", default=None,
                      help="experimental mode")
    parser.add_option("-k", "--constant", dest="constant", default=None,
                      help="a additional parameter for experimental modes (banded Covs)")   
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="Do not show parsed input options")  
    (options, filename) = parser.parse_args()
    #print(options)
    if len(filename) != 0:
        parser.error("Use the options")
    return (filename, options)

if __name__ == "__main__":
    (filename, options) = setupparams()
    
    if options.verbose:
        print(options)
    buildlog = open(options.logout,'w')
    buildlog.write('buildnormalizedmodel3.py version 0.2\n')
    buildlog.write('trainingsettxt: %s\n' % repr(options.trainingset))
    buildlog.write('normalize: %s\n' % repr(options.normalize))
    buildlog.write('reprojectmode: %s\n' % repr(options.reprojectmode))
    buildlog.write('meanshapetxt: %s\n' %repr( options.meanout))
    buildlog.write('meanshapevtk: %s\n' %repr( options.meanvtk))
    buildlog.write('eigenVectorstxt: %s\n' % repr(options.vectorout))
    buildlog.write('eigenValuestxt: %s\n' % repr(options.valueout))
    buildlog.write('covariancetxt: %s\n' % repr(options.covarout))
    buildlog.write('leaveout: %s\n' % repr(options.leaveout))


    polydata, samples, vtkfiles = readsamples(options.trainingset, options.leaveout, logout = buildlog)
    model=None
    if options.normalize=='True':
        normalizedSamples =  normalizeSamples(samples)
        if options.reprojectmode == None:
            model= buildModel(normalizedSamples)
        else:
            model = buildNormalizedModel(normalizedSamples,int(options.reprojectmode))
    elif options.normalize=='False':
        model= buildModel(samples)
    else:
        print('Error: normalize must either be True or False')
        

    numpy.savetxt(options.meanout, model['M'])
    numpy.savetxt(options.covarout, model['C'])
    if not options.meanvtk == None:
        writer=vtk.vtkPolyDataWriter()
        writer.SetFileName(options.meanvtk)
        if options.normalize=='True':
            normM = model['M'].reshape((1,-1))
            denormM = denormalizeSamples(normM)
            polydata = shapeToPolydata(polydata,denormM)
            writer.SetInput(polydata)
        else:
            writer.SetInput(shapeToPolydata(polydata, model['M']))            
        writer.Update()            
    if not options.vectorout == None:
        numpy.savetxt(options.vectorout, model['Vpartial'])
    if not options.valueout == None:
        numpy.savetxt(options.valueout, model['Dpartial'])

        
    buildlog.close()
