# Par0002 - elastix

###  Registration Description
interpatient; several transformation models; localised mutual information

###  Image data

* 3D PET
* brain
* Voxel size 2.59 x 2.59 x 8.0 mm
* Dimension: 128 x 128 x 15
* Stored as in MHD format
* Data originated from the Retrospective Image Registration Evaluation Project [1,2]
* 3D MR T1
* brain
* Voxel size 1.25 x 1.25 x 4.0 mm
* Dimension: 256 x 256 x 26
* Stored as in MHD format
* Data originated from the Retrospective Image Registration Evaluation Project [1,2]

Screen shots:

![alt-text](387px-Par0002screenshot1.png)  ![alt-text](333px-Par0002screenshot2.png)

###  Application

The grid effect is a well-known issue in image registration. It refers to the problem that the cost function contains irregularities at locations representing grid-aligning transformations, which can impede the registration process. It has often been studied in the context of interpolation artefacts [2]. In this section it is demonstrated that the sampling mechanism can solve this issue, by taking samples off the voxel grid, as suggested in [3,4].

Brain images were taken from the "Retrospective Image Registration Evaluation" project [1]. We investigated the registration of a T1-weighted MR image (moving image) to a PET image (both of patient 001).

The cost function (MI) was analysed using an exhaustive search in a single translation direction, with a step size of 0.1 mm. Linear interpolation was used to compute I_M(T_{mu}(x)). Different sampling strategies were employed for computing the cost function: all voxels, random sampling on the voxel grid, and random sampling off the voxel grid.

###  Registration settings

`elastix` version: 4.103

Command line call:


    elastix -f PET.mhd -m MR_T1.mhd -p par0002..txt -out outputdir

###  Published in

These registration are described in the publication:

S. Klein, M. Staring, K. Murphy, M.A. Viergever, J.P.W. Pluim, "`elastix`: a toolbox for intensity based medical image registration," IEEE Transactions on Medical Imaging, vol. 29, no. 1, pp. 196-205, 2010.

### Other comments

See the [elastix manual][5] for hints on how to subsequently apply the transformation to the annotated points using `transformix`.

###  References

[1] J. West, J.M. Fitzpatrick, M.Y. Wang, et al., "Comparison and evaluation of retrospective intermodality brain image registration techniques", Journal of Computer Assisted Tomography, vol. 21, no. 4, pp. 554 - 566, 1997.

[2] J.P.W. Pluim, J.B.A. Maintz and M.A. Viergever, "Interpolation artefacts in mutual information-based image registration", Computer Vision and Image Understanding, vol. 77, no. 2, pp. 211 - 232, 2000.

[3] B. Likar and F. Pernus, "A hierarchical approach to elastic registration based on mutual information", Image and Vision Computing, vol. 19, no. 1-2, pp. 33 - 44, 2001.

[4] P. Thevenaz, M. Bierlaire and M. Unser, "Halton Sampling for Image Registration Based on Mutual Information", Sampling Theory in Signal and Image Processing, vol. 7, no. 2, pp. 141 - 171, 2008.

[5]: https://github.com/SuperElastix/elastix/releases/download/5.2.0/elastix-5.2.0-manual.pdf
