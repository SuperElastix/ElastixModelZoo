# Par0052 - elastix

###  Image data

* 3D T1-weghted MRI (0.625 x 0.625 x 4.5 mm)

More details about the data are described in [1].

###  Application

Co-registration of of breast MRI screening at multiple visits of a patient.

###  Registration settings

`elastix` version: 4.7

In this work the StatisticalShapePenalty module is introduced in elastix. In order to use this as a metric you need to build elastix from source with the cmake option StatisticalShapePenalty selected.

The parameter set was determined through exhaustive search over 4050 different combinations of registration parameter combination applied to a breast MRI data deformation simulated with finite element modeling [1].

###  Known issues

N/A

###  Published in

The method and experiments are published in:

[1] Mehrabian H., Lu Y., Richmond L., Martel, A.L., [Deformable registration for longitudinal breast MRI screening][2], Journal of Digital Imaging (2018). doi.org/10.1007/s10278-018-0063-1

[2]: https://link.springer.com/article/10.1007/s10278-018-0063-1
