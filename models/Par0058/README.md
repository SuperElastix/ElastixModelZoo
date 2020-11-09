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

Description:

The translation used to register CT to CBCT in all subjects


A fixed image mask was always used, given by the FOV of the CBCT, called Cylinder.gipl

Command line call:


    elastix -f Fixed_CBCT.gipl -m Moving_CT.gipl -out ./  -mMask Cylinder.gipl -fMask Cylinder.gipl -p par0058trans.txt


###  Reference

Maspero M, Houweling AC, Savenije MH, van Heijst TC, Verhoeff JJ, Kotte AN, van den Berg CA. A single neural network for cone-beam computed tomography-based radiotherapy of head-and-neck, lung and breast cancer. Physics and Imaging in Radiation Oncology. 2020 Apr 1;14:24-31. doi:[https://doi.org/10.1016/j.phro.2020.04.002](https://doi.org/10.1016/j.phro.2020.04.002);

Maspero M, Savenije MH, van Heijst TC, Verhoeff JJ, Kotte AN, Houweling AC, van den Berg CA. CBCT-to-CT synthesis with a single neural network for head-and-neck, lung and breast cancer adaptive radiotherapy. arXiv preprint arXiv:1912.11136. 2019 Dec 23. arXiv:[https://arxiv.org/abs/1912.11136v1](https://arxiv.org/abs/1912.11136v1).
