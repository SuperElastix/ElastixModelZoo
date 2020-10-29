# Par0022 - elastix

###  Image data

* 3D T2 Cervical MR (0.625 x 0.625 x 4.5 mm)

More details about the data are described in [1].

###  Application

Inter patient registration of cervical images.

###  Registration settings

`elastix` version: 4.5

In this work the StatisticalShapePenalty module is introduced in elastix. In order to use this as a metric you need to build elastix from source with the cmake option StatisticalShapePenalty selected.

An additional script is used to generate the model from a training set. The python script together with an example training set is provided on the GitHub repo.

###  Published in

The method and experiments are published in:

[1] F.F. Berendsen et al., Free-form image registration regularized by a statistical shape model: application to organ segmentation in cervical MR, Comput. Vis. Image Understand. (2013),
