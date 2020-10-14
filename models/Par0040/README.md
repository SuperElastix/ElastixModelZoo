# Par0040 - elastix

###  Image data

* Extremity MRI
* Coronal image: intravenous injection of gadolinium contrast, T1-weighted Fast Spin-Echo sequence with frequency-selective fat saturation (voxel size: ~ 0.2 x 0.2 x 2.2 mm)
* Axial image: intravenous injection of gadolinium contrast, T1-weighted Fast Spin-Echo sequence with frequency-selective fat saturation (voxel size: ~ 0.2 x 0.2 x 3.3 mm)

###  Application

* The registration was used for fusion of coronal and axial images into a single 3D image by super-resolution reconstruction.

###  Registration settings

`elastix` version: 4.600

Parameter files:

See Github link below. 

Description:

* Aligns the axial image to the coronal image

Command line call:


    elastix -f CoronalImage.mhd -m AxialImage.mhd -p par0040affine.txt -out outputdir
