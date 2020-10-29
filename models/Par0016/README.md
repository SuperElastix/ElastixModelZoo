# Par0016 - elastix

###  Image data

* 3D chest CT
* Lung
* 16 scans (10 dir-lab, 6 extended popi-model)
* Voxel size mostly 0.97x0.97x2.5 mm for dir-lab patients // 1x1x2 for extended popi-model.
* Dimension: on average about 256 x 256 x 100 for 5 first dir-lab patients // 512 x 512 x 128 for 5 last dir-lab patient // 512 x 512 x 165 for extended popi-model

Popi-model:    
Patient Download:

dir-lab:

my masks are available here:

###  Application

Thoracic registration between End-Inhale // End-Exhale with sliding motion.

###  Registration settings

`elastix` version: svn (probably 4.6)

Command line calls:


    elastix -f 50.mhd -m 00.mhd -p params.txt -labels mm_50.mhd -fMask patient_mask_50.mhd -out outDir


###  Published in

[V. Delmon, S. Rit, R. Pinho, and D. Sarrut, "Direction dependent B-splines decomposition for the registration of sliding objects", Proceedings of the Fourth International Workshop on Pulmonary Image Analysis, Toronto, Canada, pp. 45–55, 09/2011.][1]

[1]: http://www.creatis.insa-lyon.fr/site/en/publications/DELM-11
