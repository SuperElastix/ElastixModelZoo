# Par0041 - elastix

###  Registration Description
inter-subject; similarity + B-spline transformation, advanced normalized correlation metric	

###  Image data

* Extremity MRI
* Images were obtained by application of super-resolution reconstruction (SRR) to a coronal and axial image pair (coronal image: intravenous injection of gadolinium contrast, T1-weighted Fast Spin-Echo sequence with frequency-selective fat saturation (voxel size: ~ 0.2 x 0.2 x 2.2 mm); axial image: intravenous injection of gadolinium contrast, T1-weighted Fast Spin-Echo sequence with frequency-selective fat saturation (voxel size: ~ 0.2 x 0.2 x 3.3 mm)).
* Voxel size of SRR image: ~ 0.2 x 0.2 x 0.2 mm

###  Application

* The registration was used for atlas-based segmentation of the carpal bones.

###  Registration settings

`elastix` version: 4.600

Description:

* Aligns the atlas image to the target image

Command line call:


    elastix -f TargetImage.mhd -m AtlasImage.mhd -p par0041similarity.txt -p par0041bspline.txt -out outputdir
