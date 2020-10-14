# Par0038 - elastix

###  Image data

* MR 3D multi-contrast mouse brain data with ischemic lesion
* The registration steps were carried out as described in [1] and [2]
* 3 main sets of image acquisition parameters. Those are listed in [1] and [2]
* Voxel size for the 3 main sets of T2 images: 0.12 x 0.12 x 0.50; 0,11 x 0.11 x 0.80; 0.10 x 0.10 x 0.60
* Dimensions for the 3 main sets: 128 x 128 x 16; 128 x 128 x 10; 196 x 196 x 10 & 196 x 196 x 12
* Acquired with a Bruker Biospin (Ettlingen, Germany) 7T and 11.7T scanner
* Stored in MHD format
* All data available at

###  Application

Registration was performed as one of the first steps in an automated ischemic lesion segmentation in mouse brain pipeline. Each brain scan was registered to a template brain consisting of a number of manually drawn labels. For each subject, the sum of all its echo images was used to register the scan of that particular subject to the reference brain scan. Consequently, the template labels were propagated to the individual data sets using the information provided by the deformation field for each subject-to-reference registration. The labels were used to initialize the segmentation of the whole brain and the ventricles. Registration was performed in a coarse-to-fine fashion. Initially, rigid registration was performed to compensate for translation and rotation. Afterwards, affine registration was conducted to compensate for differences in brain size. Because large deformations occur in stroke brains, a non-rigid B-spline registration was necessary to compensate for the large local changes (especially in the ipsilateral hemisphere and the ventricles region). A Gaussian image pyramid was employed in all registration steps, applying four resolutions for the rigid and two for the affine and B-spline registrations each. Normalized Correlation Coefficient was used as a similarity metric [1].

###  Registration settings

`elastix` version: 4.700

Parameter files:

See Github link below.

Description:

* par0038rigid.txt the rigid registration was used to initialize the affine registration in all subjects
* par0038affine.txt the affine registration was used to initialize the non-rigid registration in all subjects


A fixed image mask was always used.

Command line call:


    elastix -f FixedImage_i.mhd -m MovingImage_j.mhd -fMask FixedImageMask_i -p par0038.txt -out outputdir


with:  = one of {rigid, affine, bspline}

###  Published in

[1] [I.A. Mulder*, A. Khmelinskii*, O. Dzyubachyk*, N. Rieff, S. de Jong, M.J.H. Wermer, M. Hoehn, B.P.F. Lelieveldt, A.M.J.M. van den Maagdenberg, "Automated ischemic lesion segmentation in MRI mouse brain data after transient middle cerebral artery occlusion," Front. Neuroinform, Vol. 11, Issue 3, January 2017][1]

[2] [I.A. Mulder*, A. Khmelinskii*, O. Dzyubachyk*, S. de Jong, M.J.H. Wermer, M. Hoehn, B.P.F. Lelieveldt, A.M.J.M. van den Maagdenberg, "MRI mouse brain data of ischemic lesion after transient middle cerebral artery occlusion," Front. Neuroinform, Vol. 11, Issue 51, September 2017][2]

[3] [I.A. Mulder*, A. Khmelinskii*, O. Dzyubachyk*, S. de Jong, M.J.H. Wermer, M. Hoehn, B.P.F. Lelieveldt, A.M.J.M. van den Maagdenberg Data from: MRI mouse brain data of ischemic lesion after transient middle cerebral artery occlusion. Dryad Digital Repository. https://doi.org/10.5061/dryad.1m528 2017][3]

[1]: https://www.frontiersin.org/articles/10.3389/fninf.2017.00003/full
[2]: https://www.frontiersin.org/articles/10.3389/fninf.2017.00051/full
[3]: https://doi.org/10.5061/dryad.1m528
