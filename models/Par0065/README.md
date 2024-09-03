# Registration parameters for strain liver analysis.

###  Registration Description
interpatient; rigid, affine and bspline transform; advanced cross correlation


###  Image data

 - 3D MRI T1 Data healthy volunteers
 - Liver
 - 3 different states: end-expiration, end-inspiration, drinking of 1.5l of water
 - Resolution: 1.5x1.5x3mm^3

###  Application

These parameters are used to register the livers at end-inspiration and 1.5l water drinking to end-expiration. From the deformation field volumetric strain and octahedral shear strain [1] is determined.

###  Registration settings

Livers are aligned using rigid transform first. Next an affine and bspline transform is performed on the livers.

- Elastix version: 5.0.0
- ITKElastix version: 0.21.0

Python call:

Do rigid transform:
`
elastix_object = itk.ElastixRegistrationMethod.New(fixed_image, moving_image)
elastix_object.SetParameterObject(parameter_object_rigid)
elastix_object.UpdateLargestPossibleRegion()
transformed_image = elastix_object.GetOutput()
transformed_parameters = elastix_object.GetTransformParameterObject()
`

Do affine, bspline transfrom:
`
elastix_object = itk.ElastixRegistrationMethod.New(fixed_image, transformed_image)
elastix_object.SetParameterObject(parameter_object_affine_bspline)
elastix_object.UpdateLargestPossibleRegion()
transformed_image = elastix_object.GetOutput()
transformed_parameters = elastix_object.GetTransformParameterObject()
`

###  Published in

Noah Jaitner, Yasmine Safraou, Matthias Anders, Jakob Schattenfroh, Tom Meyer, Biru Huang, Jakob Jordan, Oliver Boehm, Alfonso Caiazzo, Tobias Schaeffter, Jing Guo, Ingolf Sack (2024), Non-invasive assessment of portal pressure by combined measurement of volumetric strain and stiffness of in vivo human liver (submitted)

###  References

[1] McGarry, M.D.J., et al., An octahedral shear strain-based measure of SNR for 3D MR elastography. Physics in Medicine and Biology, 2011. 56(13): p. N153-N164.
