# Par0032 - elastix

###  Image data

* 3D breast T1-weighted DCE-MRI
* Breast
* Voxel size mostly 0.7x0.7x1.3 mm.
* 1 pre-contrast volume + 4-5 post-contrast time points


MRI images were acquired in 1.5 or 3 Tesla Siemens scanner (Magnetom Avanto, Magnetom Sonata, Magnetom Simphony and Magnetom Trio)

###  Application

Motion correction in Dynamic Contrast-Enhanced MRI of the breast

###  Registration settings

`elastix` version: 4.7

Parameter File:

See Github link below. 

Command line calls:


    elastix -f preContrast.dcm -m postContrastX.dcm -p params.txt -out outDir


###  Published in

A. Gubern-Mérida; R. Marti; J. Melendez; J. Hauth; R. Mann; N. Karssemeijer and B. Platel. "Automated localization of breast cancer in DCE-MRI", Medical Image Analysis 2015;20:265-274.
