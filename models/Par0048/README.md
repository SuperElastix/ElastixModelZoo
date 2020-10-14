# Par0048 - elastix

###  Image data

![6-point-Dixon-elastix-wiki.jpg][1]

* 3D 6-point Dixon MR volumes; pre- and post-cooling
* Stored in meta-image format

###  Application

* The registration was used for aligning pre- and post-cooling scans of the same subject

###  Registration settings

`elastix` version: 4.800

Parameter files:

See Github link below.

Description:

* par0048elastic.txt elastic registration was used to register the post-cooling volume to the pre-cooling one

Command line call:


    elastix -f preCooling.mhd -m postCooling.mhd -p par0048elastic.txt -out outputdir


###  Submitted manuscript

[1] G. Abreu-Vieira*, J. Burakiewicz*, L.G.M. Janssen, K.J. Nahon, M.R. Boon, O. Dzyubachyk, A.G. Webb, H.E. Kan, P.C.N. Rensen. "Human brown adipose tissue lipid mapping by MRI and its heterogenic changes in volume, mass and energy content after cold exposure"

[1]: http://elastix.bigr.nl/wiki/images/5/59/6-point-Dixon-elastix-wiki.jpg
