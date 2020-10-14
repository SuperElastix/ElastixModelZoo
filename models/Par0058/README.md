# Par0058 - elastix

###  Subjects

Head-neck, lung and breast cancer patients acquired between 2016-2018.

###  Image data

The values are reported in RL, AP, FH directions.

**CBCT**

Acquired on Synergy Linac with XVI (v5.0.2b72 Elekta AB, Sweden)

* Voxel size: 1x1x1 mm3
* Vp = 100-120kV; ms = 10-40; mA = 10-25;
* FOV = 27-41x27-41x13-79 cm3
* Stored in gipl format

**CT**

Acquired on Brilliance Big Bore (Philips Healthcare, Ohio, USA).

* Voxel size = 0.6-1.37x0.6-1.37x1-3 mm3
* kVp = 120kV; ms = 900-1800; mA = 31-271;
* FOV = 29-70x29-70x23-180 cm3
* Stored in gipl format

###  Application

For each subject, each CT was translated and resampled to CBCT to minimise set-up errors.

###  Registration settings

`elastix` version: 4.700

Parameter files:

See Github link below.

Description:

The translation used to register CT to CBCT in all subjects


A fixed image mask was always used, given by the FOV of the CBCT, called Cylinder.gipl

Command line call:


    elastix -f Fixed_CBCT.gipl -m Moving_CT.gipl -out ./  -mMask Cylinder.gipl -fMask Cylinder.gipl -p par0058trans.txt


###  Submitted to

[1] XXX (the journal where the work has been submitted is double blind, so authors have been omitted) et al. 2019 [WIP, it will be updated upon acceptance]
