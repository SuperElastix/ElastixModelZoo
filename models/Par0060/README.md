# Par0060 - elastix

###  Image data

* 2D cine-MRI acquired at 1.5T with 50-300 frames ('dynamics') per imaging session.
* Imaging parameters: 2D sagittal balanced steady-state free precession sequence (bSSFP). Relaxation time: 2.8 ms, echo time: 1.4 ms, flip angle: 50 degrees, FOV: 320x320 mm, voxel spacing: 1.42x.1.42 mm, slice thickness: 7 mm, readout direction: feet-head, bandwidth: 724-2034 Hz/px. Temporal resolution of each dynamic was 500-570 ms;

###  Application

The registration was used to align organs in the abdomen of sequential cine-MR dynamics to the reference dynamic, randomly chosen from the cine after entering the steady-state. This registration was used to obtain deformable intrafraction motion from 2D cine-MR images as a potential deep learning ground-truth to learn deformtion vector fields.

###  Registration settings

`elastix` version: 4.800

Parameter files:

See Github link below.

Command line call:


    elastix -f  -m  -p param_rigid.txt -p param_affine.txt -p param_bspline.txt -out


where  is the path to fixed image, the reference cine MRI dynamic. The  is the path to a cine-MR dynamic of the same imaging session.  is the output directory.

###  Known issues

N/A

###  Submitted for publication in

Maarten L. Terpstra, Matteo Maspero, Federico d'Agata, Bjorn Stemkens, Martijn P.W. Intven, Jan J.W. Lagendijk, Cornelis A.T. van den Berg, and Rob H.N. Tijssen, Deep learning-based image reconstruction and motion estimation from undersampled radial k-space for real-time MRI-guided radiotherapy, Physics in Medicine and Biology (submitted), February 2020.
