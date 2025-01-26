# Par0008 - elastix

###  Registration Description
intrapatient; B-spline transformation; mutual information	

###  Image data

* 3D chest CT
* Lung
* Breath-hold inspiration scans
* Voxel size resampled to 0.7x0.7x~0.7 mm
* Dimension: 512 x 512 x ~500 (sub-sampled to 256 x 256 x ~200 such that voxels were isotropic)


Screen shot:

![alt-text](Keelin_Par0008.jpg)

Comments: A sample of two temporal inspiration scans from the same patient.

###  Application

Registration of follow-up inspiration CT scans has multiple applications including improving ease of visual comparison and enabling automatic comparisons. Specific medical applications are not described in this article.

###  Registration settings

`elastix` version: 4.0

###  Published in

These registration are described in the publication:

K. Murphy, B. van Ginneken, J.P.W. Pluim, S. Klein, and M. Staring, Semi-Automatic Reference Standard Construction for Quantitative Evaluation of Lung CT Registration, in MICCAI, ser. Lecture Notes in Computer Science, vol. 5242, 2008, pp. 1006 – 1013.

### Note

"Parameters.Par0008.elastic.txt" has accidentally specified the parameters `BSplineInterpolationOrder` and `FinalBSplineInterpolationOrder` twice, with different values. This may cause an error in elastix versions built after October 13, 2009 (more specifically, after commit https://github.com/SuperElastix/elastix/commit/2c72f70c738c7f95067747af486216223e1e2268), saying  "The parameter ... is specified more than once." Older elastix versions probably just ignore the first occurrences of those parameters. 

###  References

[1] K. Murphy, B. van Ginneken, J. P. W. Pluim, S. Klein, and M. Staring, "Semi-automatic reference standard construction for quantitative evaluation of lung CT registration," in MICCAI, ser. Lecture Notes in Computer Science, vol. 5242, 2008, pp. 1006 – 1013.
