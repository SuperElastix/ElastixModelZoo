# Par0055 - elastix

###  Registration Description
intra-subject cine-MRI motion; rigid transformation

###  Image data

* 3D cine-MRI acquired at 3T with 55 frames ('dynamics') per imaging session.
* Imaging parameters: 3D balanced steady-state free precession sequence (bSSFP) with fat suppression. Relaxation time: 4 ms, echo time: 1.98 ms, flip angle: 30 degree, FOV: 384x384x120 mm, acquired voxel spacing: 2x2x2 mm, reconstructed voxel spacing 0.96x0.96x2 mm, bandwidth: 1768.3 Hz/px, turbo factor 51, SPAIR (TR 427 ms, Inversion delay 122 ms, offset 220 Hz, fold-over direction Right-left). Temporal resolution of each dynamic was 10.7 second;

###  Application

The registration was used to align the prostate of sequential cine-MR dynamics to the first (fixed) dynamic, at time point 0. This registration was used to obtain prostate intrafraction motion from 3D cine-MR images. The first translation was applied and then an Euler transformation, obtaining the translation and rotation.

###  Registration settings

`elastix` version: 4.700

Command line call:


    elastix -f TargetImage.mhd -m MovingImage.mhd -p translation.txt -p eulertransformation.txt -out outputdir


where "TargetImage" is the fixed image, the cine-MR dynamic at timepoint 0. The "MovingImage" is a cine-MR dynamic of the same imaging session. "Outputdir" is the output directory.

###  Published in

de Muinck Keizer DM, Kerkmeijer LG, Maspero M, Andreychenko A, van Zyp JV, Van den Berg CA, Raaymakers BW, Lagendijk JJ, de Boer JC. Soft-tissue prostate intrafraction motion tracking in 3D cine-MR for MR-guided radiotherapy. Physics in Medicine & Biology. 2019 Dec 5;64(23):235008. doi:[https://doi.org/10.1088/1361-6560/ab5539](https://doi.org/10.1088/1361-6560/ab5539).
