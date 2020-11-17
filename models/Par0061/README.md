# Par0061 - elastix

###  Registration Description
Intrapatient, rigid transformation

###  Subjects

39 patients with lymph node metastases in pelvic or para-aortic region, each patient underwent 5 SBRT treatment sessions except 1 patient who underwent 2 cycles, so 10 SBRT treatment sessions in total. MR images of the pelvic or abdominal region were obtained at the start, during and after each treatment session.

###  Image data

For each patient, typically one of the sequences below was used for each scan at start, mid and end of each treatment session (so monomodal image registration).

**T1 MRI**

Acquired on a 1.5T MR-linac (Elekta Unity).

Transverse 3D T1-weighted FFE scan with an acquisition time of 2 min (TR 11 ms, TE 4.6 ms, acquired voxel size 1.5 x 1.5 x 2.0 mm3, FOV 400 x 400 x 300 mm3)

**T2 MRI**

Acquired on a 1.5T MR-linac (Elekta Unity).

Transverse 3D T2-weighted TSE scan with an acquisition time of 3min40s (TR 1500 ms, TE 124 ms, acquired voxel size 1.3 x 1.3 x 2.0 mm3, FOV 400 x 400 x 300 mm3)

###  Application

For each treatment session, the mid-treatment (PV) and end (post) scans were registered to the start (pre) scan of that treatment session.

###  Registration settings

`Elastix` version: 4.8

Description:

The rigid registration that was used to register cropped PV or post scans to the cropped pre scan. A fixed mask was used that encompassed 1 cm around the pre-scan bony anatomy in the region close to the target lymph node (bone mask cropped at 2 cm towards cranial and caudal from the planning target volume).

Command line call:


    elastix -p  par0061.txt –f pre_scan.mhd -m post_scan.mhd -out output_dir -fMask bone_mask.mhd


###  Published in

Werensteijn-Honingh et al. (2020), Impact of a vacuum cushion on intrafraction motion during online adaptive MR-guided SBRT, submitted.
