# Par0034 - elastix

###  Image data

* _In vivo_ Cerebral Blood Flow (CBF) MRI mouse data
* The registration steps were carried out with the second image of the CBF dataset
* Voxel size 0.296291 x 0.3
* Acquired with a Bruker Biospin (Ettlingen, Germany) 7T scanner
* Stored in MHD format
* [1]


Screen shot:

![386 × 485px][1]

An example of the co-registered mouse brain data: on the right you see the used template image.

###  Application

###  Registration settings

`elastix` version: 4.700

Parameter files:

See Github link below.

Description:

* par0034rigid.txt the rigid registration was used to initialize the affine registration in all subjects
* par0034affine.txt the affine registration was used to initialize the non-rigid registration in all subjects

A template image was registered to all data. The template image was the moving image.

Command line call:


    elastix -f FixedImage_i.mhd -m MovingImage_j.mhd -p par0034.txt -out outputdir


with:  = one of {rigid, affine, bspline}

###  Published in

[1] [D.I. Bink _et al.,_ "," _in preparation_ 2016]

[1]: http://elastix.bigr.nl/wiki/images/2/25/Bink_elastix_wiki_IN_VIVO_CBF_screenshot.png
