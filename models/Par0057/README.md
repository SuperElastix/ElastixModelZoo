# Par0057 - elastix

###  Image data

Clinical 4D dynamic contrast enhanced (DCE) MR images and diffusion weighted (DW) MR images with three b-values, both with the clinical focus on the liver. The mean DCE MR images is calculated from all the DCE MR images and used as fixed image. The DW MR image with the lowest b-value is resized to the dimensions of the mean DCE MR image and used as moving image.

###  Application

Registration of DW MR images to the DCE MR image space.

###  Registration settings

`elastix` version: 4.801

Parameter files:

See Github link below.

###  Command line calls

To used the rigid registration followed by the b-spline registration, the following command is used:


    elastix -f  -m  -p  -p  -fMask  -out

where  is the mean DCE MR image,  is the resized DW MR image with the lowest b-value, and  is a liver mask created before registration to focus the registration on the liver region.

The remaining DW MR images can be transformed to the DCE MR image space by using the 'TransformParameters.1.txt' output in the function . The following command can be used:


    transformix -in  -out  -tp

where  is the resized DW MR image.
