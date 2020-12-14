# General

<tt>elastix</tt> image registration of anatomical MR scans of esophageal cancer tumors

### Image data

* Respiratory-triggered transversal anatomical T2-weighted scans on different timepoints (interfraction data)
* Imaging parameters: TR/TE = 1604/100ms, resolution = 0.67x0.67x6.48mm3, FOV: 336x336x28, flip angle: 90 degrees
* Clinical target volume is contoured and a mask is used as input in this workflow

### Application

This multi-step registration is used to register follow-up images to the reference MRI. Patients are positioned based on a rigid bone-match registration with help of a box around the vertebrae. The second registration step consists of a mutual information registration. The final registration step is a kappa-statistic on a mask of the clinical target volume (CTV) combined with a bending penalty.

### Registration settings

<tt>elastix</tt> version: 4.700

Parameter files:
* Parameters_Translation.txt
* Parameters_Rigid.txt
* DIR-step1.txt
* DIR-step2.txt


Command line call:


<code>
elastix -f baseline.gipl -m follow-up.gipl -p Parameters_Translation.txt -out . -fMask baseline_bonemask.gipl -mMask follow-up_bonemask.gipl
mv TransformParameters.0.txt TP_Translation_follow-up.txt
elastix -f baseline.gipl -m follow-up.gipl -p Parameters_Rigid.txt -out . -fMask baseline_bonemask.gipl -mMask follow-up_bonemask.gipl -t0 TP_Translation_follow-up.txt
mv TransformParameters.0.txt TP_Euler_follow-up.txt
elastix -f baseline.gipl -m follow-up.gipl -p DIR-step1.txt -out . -t0 TP_Euler_follow-up.txt
mv TransformParameters.0.txt TP_DIR_step1.txt
elastix -f0 baseline_ctvmask.gipl -m0 follow-up_ctvmask.gipl -p DIR-step2.txt -out . -t0 TP_DIR_step1.txt
</code>

where "baseline.gipl" is the fixed image, the reference MRI. The "follow-up.gipl" is the follow-up MRI.

### Known issues

N/A

### Submitted for publication in

Boekhoff et al. Submitted
