# Par0054 - elastix

###  Image data

* 3D thoracic CT (inhale/exhale phases from 4DCT)
* Voxel size 1 x 1 x 3 mm
* Dimension 512 x 512 x 114

The sample CT dataset is available for [download](https://github.com/guycl/elastix_examples/tree/master/sstvd).

###  Application

Registration of intra-patient thoracic CT scans in the presence of respiratory motion causing compression/expansion of lung parenchyma

###  Registration settings

`elastix` version: 4.9

The SumSquaredTissueVolumeDifference metric was implemented in `elastix` during the course of this work.

Command line call:


    elastix -p par0054_sstvd.txt -f scan_inhale.mhd -m scan_exhale.mhd -out ./output


###  Known issues

N/A

###  Published in

Registrations using the SSTVD metric in `elastix` were used in the following publication (corresponding to registration 1 in table 1):

Christopher L. Guy, Elizabeth Weiss, Gary E. Christensen, Nuzhat Jan, and Geoffrey D. Hugo, "CALIPER: A deformable image registration algorithm for large geometric changes during radiotherapy for locally advanced non-small cell lung cancer," Medical Physics, 45 (6), June 2018. doi.org/10.1002/mp.12891
