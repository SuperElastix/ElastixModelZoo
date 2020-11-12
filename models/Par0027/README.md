# Par0027 - elastix

###  Registration Description
intra patient; rigid + B-spline transformation; mutual information, multi parametric mutual information	

###  Image data

CT and MR images of the head and neck (HN) region

* CT: 0.98 x 0.98 x 2.5 mm^3
* MR: 0.68 x 0.68 x 3 mm^3, T1 and T2-weighted

Both MR and CT images were acquired with the patient fixed in treatment (radiotherapy) position. Detailed information is provided in publication listed below.

###  Application

Intra-patient deformable registration of CT and MR images of the HN region for the integration of (PET/)MRI data into radiotherapy treatment planning.

###  Registration settings

`elastix` version: 4.6

The images are first aligned using an automatically detected point in the neck region. Than rigid registration followed by deformable registration was applied. We tested the use of multi-parametric registration using simultaneously registering T1w and T2w images with CT. For this we used a MultiMetricMultiResolutionRegistration and we optimized the weight given to T1w and T2w images to compute the combined metric.

A leave-one-out parameter optimization was done for the parameters: nr. of resolution levels, BSpline control point grid spacing and the optimal weights for the combined metric.

Fixed and moving image masks have been used in all the experiments. In the case of multiparametric registration we specified masks for both the moving MR (T1w and T2w) images. i.e.


    elastix -f  -m0  -m1  -out  -p  -t0  -fMask  -mMask0  -mMask1  

###  Published in

V. Fortunati, R.F. Verhaart, F. Angeloni, A. van der Lugt, W.J. Niessen, J.F. Veenland, M.M. Paulides and T. van Walsum, Feasibility of Multimodal Deformable Registration for Head and Neck Tumor Treatment Planning, Int. J. Radiation Oncology Biology and physics 90, 85-93 (2014)
