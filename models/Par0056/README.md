# Par0056 - elastix

###  Image data

* CBCT mouse lung data
* The registration steps were carried out as described in [1]
* Voxel size: 0.1x0.1x0.1mm3
* Acquired at 100kV with a X-RAD 225Cx µIGRT system (Precision X-ray Inc., North Branton, US)
* Stored in MHD format

###  Application

For each subject, each baseline scan (time-point 0 wks) was registered to a template scan consisting of two manually drawn labels: one for the right lung and one for the left lung. Those labels were drawn by avoiding the large vessels and the heart (Panel A in Sup-Figure S1). After that, for each subject, the follow-up scans performed post-irradiation (time-points 8, 34, 36, 37, and 40 wks) were registered to the correspondent baseline scan. The template labels were propagated to each scan and the radiodensity values were calculated within those labels. Registration was performed in a coarse-to-fine fashion. Initially, rigid registration was performed to compensate for possible translation and rotation. Afterwards, affine registration was conducted to compensate for possible differences in lung size. A two resolution Gaussian image pyramid was employed in both the rigid and affine registration steps. Mutual information was used as a similarity metric [1].

###  Registration settings

`elastix` version: 4.800

Parameter files:

See Github link below.

Description:

* par0056rigid.txt the rigid registration was used to initialize the affine registration in all subjects


A fixed image mask was always used.

Command line call:


    elastix -f FixedImage_i.mhd -m MovingImage_j.mhd -fMask FixedImageMask_i -p par0056.txt -out outputdir


with:  = one of {rigid, affine}

###  Published in

[1] [D. van Berlo, A. Khmelinskii*, A. Gasparini*, F. J. Salguero, B. Floot, N. de Wit, M. van de Ven, J. Y. Song, R. P. Coppes, M. Verheij, J. J. Sonke and C. Vens, "Micro Cone Beam Computed Tomography for sensitive assessment of radiation-induced late lung toxicity in preclinical models," accepted, Radiotherapy & Oncology, 2019][1]

[1]: https://www.sciencedirect.com/science/article/pii/S0167814019304062?via%3Dihub
