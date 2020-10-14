# Par0039 - elastix

###  Image data

Real quantitative MRI (qMRI) image data:

* 3D T1MOLLI-HEART: Porcine hearts with a transmural myocardial infarction of the lateral wall were acquired using modified Look-Locker inversion recovery (MOLLI) sequence.
* 4D T1VFA-CAROTID: Carotids were acquired using a 3D improved motion-sensitized driven-equilibrium prepared black-blood turbo field echo sequence.
* 4D ADC-ABDOMEN: Abdomen were acquired using a diffusion weighted sequence. Diffusion weighting was applied in three orthogonal directions aligned with the read, phase and slice directions.
* 4D DTI-BRAIN: Brains were acquired using a diffusion weighted sequence with a single b-value and multiple gradient directions.
* 4D DCE-ABDOMEN: Abdomen were acquired with a spoiled gradient echo sequence using a contrast agent.

To evaluate how the methods perform with different qMRI models, in a setting with known ground truth, we created synthetic data based on real qMRI data. To save computation time, we extracted a 2D slice from a single subject for each of the qMRI applications. The synthetic data can be downloaded on Github, see link below:

And a dummy synthetic dataset was created, using a fake model, see Github link:

More details about the data and the corresponding qMRI models are described in [1].

###  Application

Motion and/or geometrical distortion compensation for quantitative MRI.

###  Registration settings

`elastix` version: 4.801

Parameter files:

See Github link below.

###  Command line calls

For groupwise registration one should use the following command line call:


    elastix -f  -m  -p  -out

where  is the entire group of images that are acquired in a single quantitative MRI acquisition. Note that the fixed and moving image should be the same. The fixed image is not used for the registration, but acts as a dummy to prevent elastix throwing error messages. When a mask is used to restrict the samples to be taken from a certain region, it can be added with -fMask.

The reference frame for this alignment lies somewhere in between the transformations of all the images, due to the constraint applied to the transform parameters. For more information see [1].

###  Mask related issues

The groupwise registration with moving masks sometimes gives undesirable and inexplicable results. The current recommendation is to use a fixed mask only, which only restricts the sampling to a certain region in the fixed image. Note that in the groupwise metrics samples are taken from the first image in the group of images and are then copied to all the other images. A sample is only accepted when it exists in all images of the group.

###  Published in

The method and experiments are published in:

[1] [10.1016/j.media.2015.12.004 PCA-based groupwise image registration for quantitative MRI, W. Huizinga, D.H.J. Poot, J.-M. Guyader, R. Klaassen, B.F. Coolen, M. van Kranenburg, R.J.M. van Geunse, A. Uitterdijk, M. Polfliet, J. Vandemeulebroucke, A. Leemans, W.J. Niessena, S. Klein, Medical Image Analysis, in press]
