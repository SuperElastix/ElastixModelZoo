# Par0057 - elastix

###  Image data

Clinical 4D dynamic contrast enhanced (DCE) MR images and diffusion weighted (DW) MR images with three b-values, both with the clinical focus on the liver. The mean DCE MR images is calculated from all the DCE MR images and used as fixed image. The DW MR image with the lowest b-value is resized to the dimensions of the mean DCE MR image and used as moving image.

###  Application

Registration of DW MR images to the DCE MR image space.

###  Registration settings

`elastix` version: 4.801

###  Command line calls

To used the rigid registration followed by the b-spline registration, the following command is used:


    elastix -f <fixed image> -m <moving image> -p <par filename rigid> -p <par filename b-spline> -fMask <liver mask>  -out <output dir>

where <fixed image> is the mean DCE MR image, <moving image> is the resized DW MR image with the lowest b-value, and <liver mask> is a liver mask created before registration to focus the registration on the liver region.

The remaining DW MR images can be transformed to the DCE MR image space by using the 'TransformParameters.1.txt' output in the function <transformix>. The following command can be used:


    transformix -in <moving image> -out <output dir> -tp <transform parameters>

where <moving image> is the resized DW MR image.
