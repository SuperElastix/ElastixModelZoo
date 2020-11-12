# Par0009 - elastix

###  Registration Description
interpatient; B-spline transformation; mutual information	

###  Image data

* 3D brain MRI, T1-weighted
* IBSR public dataset (http://www.cma.mgh.harvard.edu/ibsr/)
* 1.5 slice thickness
* Dimension: 256 x 256 x 128

###  Application

Registration that can be used for atlas-based segmentation of brain structures. Transformations should be saved and then applied on the atlas images to obtain a segmentation of the target image. Segmentations from different atlas images can be combined to achieve higher accuracy, as explained in [1].

###  Registration settings

`elastix` version: 4.0

###  Published in

These registration steps are described in the publication:

Artaechevarria X, Munoz-Barrutia A, Ortiz-de-Solorzano C., "Combination strategies in multi-atlas image segmentation: application to brain MR data," IEEE Trans Med Imaging. 2009 Aug;28(8):1266-77.

###  References

[1] Artaechevarria X, Munoz-Barrutia A, Ortiz-de-Solorzano C., "Combination strategies in multi-atlas image segmentation: application to brain MR data," IEEE Trans Med Imaging. 2009 Aug;28(8):1266-77.
