# Par0047 - elastix

###  Image data

Clinical 4D dynamic contrast enhanced MR images with focus on the liver.

###  Application

Motion correction for contrast enhanced time series of the abdomen.

###  Registration settings

`elastix` version: 4.801

Parameter files:

See Github link below

* Groupwise Registration, using PCAmetric2

See Github link below

###  Command line calls

For groupwise registration one should use the following command line call:


    elastix -f <4D DCE-MRI image> -m <4D DCE-MRI image> -p  -out

where <4D DCE-MRI image> is the entire group of images that are acquired in a single DCE-MRI acquisition. Note that the fixed and moving image should be the same. The fixed image is not used for the registration, but acts as a dummy to prevent elastix throwing error messages.

###  Publish

The work is published in:

M. J. A. Jansen, H. J. Kuijf, W. B. Veldhuis, F. J. Wessels, M. van Leeuwen, and J. P. W. Pluim, " Evaluation of motion correction for clinical dynamic contrast enhanced MRI of the liver," Phys. Med. Biol., 62(19), pp. 7556–7568, 2017.

DOI: [10.1088/1361-6560/aa8848][3]

[1]: http://elastix.bigr.nl/wiki/images/9/9f/Par0047Pairwise.txt "Par0047Pairwise.txt"
[2]: http://elastix.bigr.nl/wiki/images/7/73/Par0047Groupwise.txt "Par0047Groupwise.txt"
[3]: https://iopscience.iop.org/article/10.1088/1361-6560/aa8848
