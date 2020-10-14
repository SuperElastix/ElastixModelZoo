# Par0045 - elastix

###  Image data

* MR ATT, pCASL, te-pCASL, T2w, T1 mouse brain data
* Image acquisition parameters described in [1]
* Voxel size for for T2wdata: INSERT NUMBER 128 x 128 x 16
* Voxel size for for perfusion data: INSERT NUMBER 128 x 128 x 16
* Voxel size for for T1 data: INSERT NUMBER 128 x 128 x 16
* Dimensions for T2wdata: INSERT NUMBER 128 x 128 x 16;
* Dimensions for perfusion data: INSERT NUMBER 128 x 128 x 16;
* Dimensions for T1 data: INSERT NUMBER 128 x 128 x 16;
* Acquired with a Bruker Biospin (Ettlingen, Germany) 7T scanner
* Stored in MHD format

###  Application

To compensate for possible motion during standard pCASL and te‐pCASL acquisitions, all repetitions were registered to the first EPI acquisition. ROIs for the auditory/visual cortex, hippocampus, motor cortex, sensory cortex, striatum and thalamus were delineated manually on an anatomical T2w image of a randomly selected animal (reference T2w image) based on the Franklin–Paxinos mouse brain atlas. The T2w images of the remaining animals were registered to the above‐mentioned reference T2w image and all ROIs were propagated to each animal's corresponding T2w image. For each animal, all sequences (te‐pCASL, T1t map, T2w image) were registered to the standard pCASL space. The registration of the T2w images to the standard pCASL space allowed the propagation of the anatomical ROIs to all the remaining MRI sequences. The registration was performed in a coarse‐to‐fine manner [1].

###  Registration settings

`elastix` version: 4.700

Parameter files:

See Github link below.

Description:

* par0045rigid.txt the rigid registration was used to initialize the affine registration in all subjects
* par0045affine.txt the affine registration was used to initialize the non-rigid registration in all subjects


A fixed image mask was always used.

Command line call:


    elastix -f FixedImage_i.mhd -m MovingImage_j.mhd -fMask FixedImageMask_i -p par0038.txt -out outputdir


with:  = one of {rigid, affine, bspline}

###  Published in

[1] [L. Hirschler*, L.P. Munting*, A. Khmelinskii, W.M. Teeuwisse, E. Suidgeest, J.M. Warnking, L. van der Weerd, E.L. Barbier, M.J.P. Osch, "Transit time mapping in the mouse brain using time-encoded pCASL," NMR in Biomedicine, e3855, November 2017][1]

[1]: http://onlinelibrary.wiley.com/doi/10.1002/nbm.3855/full
