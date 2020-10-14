# Par0059 - elastix

###  Subjects

CT and MR images in the pelvic region.

###  Image data

**MR**

Acquired on a 3T Philips Ingenia.

* In-phase image from a 3D T1-weighted multi-echo gradient echo sequence
* Voxel size : 0.97x0.97x1 mm3
* TE/TR = 2.1ms / 6.5ms
* Voxel size: 1x1x1 mm3

**CT**

Acquired on Brilliance Big Bore.

* Pixel spacing : 0.3 to 0.7 mm
* Slice spacing : 3 mm

###  Application

MR and CT scans were acquired for 27 male patient for radiotherapy purposes. Non-rigid registration was used to align and resample the MR and CT volumes to train a deep learning model for synthetic CT generation. MR was the fixed image and CT the moving image.

###  Registration settings

`Elastix` version: 4.9


Parameter files:

See Github link below.

Description:

* Aligns and resamples MR and CT images


Command line call:


    elastix -p  par0059_rigid.txt -p par0059_bspline.txt –f MR_image.nii.gz -m CT_image.nii.gz -out output_dir -fMask MR_body_mask.nii.gz


###  Reference

Florkow et al. (2019), Deep learning-based MR-to-CT synthesis: the influence of varying gradient echo-based MR images as input channels, under submission
