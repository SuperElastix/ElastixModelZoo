# Par0051 - elastix

###  Image data

* Extremity MRI
* Images were obtained by application of super-resolution reconstruction (SRR) to a coronal and axial image pair (coronal image: intravenous injection of gadolinium contrast, T1-weighted Fast Spin-Echo sequence with frequency-selective fat saturation (voxel size: ~ 0.2 x 0.2 x 2.2 mm); axial image: intravenous injection of gadolinium contrast, T1-weighted Fast Spin-Echo sequence with frequency-selective fat saturation (voxel size: ~ 0.2 x 0.2 x 3.3 mm)).
* Voxel size of SRR image: ~ 0.2 x 0.2 x 0.2 mm

###  Application

* The registration was used for atlas-based segmentation of carpal bones, distal radius/ulna, and locating of initial landmarks for flexor and extensor tendons.

###  Registration settings

`elastix` version: 4.800

Parameter files:

See Github link below.

Description:

* Aligns the atlas image to the target image

Command line call:


    elastix -f TargetImage.mhd -m AtlasImage.mhd -p par0051similarity.txt -p par0051bspline.txt -out outputdir
