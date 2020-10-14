# Par0033 - elastix

###  Image data

* _Ex vivo_ MRI on mouse skulls to image the brain
* T1 3D Flash sequence
* TR 15ms, TE 5.3ms, NA 12, matrix 256*186*186, FOV 18*18*13cm, hermite FA 30º, resolution 70µm/pixel, total scan time 58min48s
* Voxel size 0.0703125 x 0.07 x 0.07
* Acquired with a Bruker Biospin (Ettlingen, Germany) 7T scanner
* With a circular polarized MRI transceiver coil for 1H with an inner diameter of 23 mm and Paravision 5.1 software
* Stored in MHD format
* [1, 2]


Screen shot:

![386 × 485px][1]

An example of the co-registered mouse brain data: on the left you see the used template.

###  Application

###  Registration settings

`elastix` version: 4.500

Parameter files:

See Github link below.

Description:

* par0033rigid.txt the rigid registration was used to initialize the affine registration in all subjects
* par0033similarity.txt the affine registration was used to initialize the non-rigid registration in all subjects

All the data was registerd to a template image. The template image was the fixed image. A fixed image mask was always used.

Command line call:


    elastix -f FixedImage_i.mhd -m MovingImage_j.mhd -fMask FixedImageMask_i -p par0033.txt -out outputdir


with:  = one of {rigid, similarity, bspline}

###  Published in

[1] [D.I. Bink, K. Ritz, C. Mackaaij, A. Khmelinskii, O.J. de Boer, L.M. Gierman, J.C. Sluimer, L. van der Weerd, M.J.A.P. Daemen, "Neuropathology in mouse models for atherosclerosis," _Submitted_ 2016]

[2] [B. Kogelman _et al.,_ "," _in preparation_ 2016]

[1]: http://elastix.bigr.nl/wiki/images/d/dd/Bink_elastix_wiki_EX_VIVO_screenshot.png
