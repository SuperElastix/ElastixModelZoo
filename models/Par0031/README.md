# Par0031 - elastix

###  Image data

* 3D chest CT
* Lung
* 10 scans (dir-lab[[1]][1])
* Voxel size mostly 0.97x0.97x2.5 mm.
* Dimension: on average about 256 x 256 x 100 for 5 first dir-lab patients // 512 x 512 x 128 for 5 last dir-lab patient

The masks and sliding region definitions from Delmon et al. were used as they were kindly made publicly available (see Par0016).

###  Application

Thoracic registration between End-Inhale // End-Exhale with sliding motion.

###  Registration settings

`elastix` version: 4.8 (paper dates from 4.6)


Command line calls:


    elastix -f 50.mhd -m 00.mhd -p params.txt -labels mm_50.mhd -fMask patient_mask_50.mhd -out outDir


###  Published in

F. F. Berendsen; A. N. T. J. Kotte; M. A. Viergever; J. P. W. Pluim, "Registration of organs with sliding interfaces and changing topologies", Proc. SPIE 9034, Medical Imaging 2014: Image Processing, 90340E (21 March 2014); doi: 10.1117/12.2043447

[1]: http://www.dir-lab.com/
