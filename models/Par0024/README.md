# Par0024 - elastix

###  Image data

* 3D T2 Cervical MR (0.625 x 0.625 x 4.5/3.0 mm)

More details about the data are described in [1].

###  Application

Registration of two images where a structure is present in one of them, but absent in the other. The method was used for (intra patient) registration of cervical images, where in one of the images a large volume was occupied by a brachytherapy applicator.

###  Registration settings

`elastix` version: 4.7

In this work the MissingStucturePenalty [1] module is introduced in `elastix`. The code is committed to the repository; at this moment it requires a build from source with the option USE_MissingStructurePenalty ticked in CMake.

Example of the minimal settings required for the MissingStructurePenalty:


    (Registration "MultiMetricMultiResolutionRegistration")

    (Metric "AdvancedNormalizedCorrelation" "MissingStructurePenalty" )

    (Metric0Weight 1 )

    (Metric1Weight 0.00000001 )

    //Optional (WriteResultMeshAfterEachIteration "true" )

    //Optional (WriteResultMeshAfterEachResolution "true" )


To supply this metric with a triangulated surface mesh (.vtk file) use the commandline option: -fmesh, where  is replaced by a letter from the range [A-Z] and  the index number of the metric in the multi-metric registration. In the minimal example the MissingStructurePenalty is the second metric in the multi-metric registration (MetricIndex:1, starting from 0)

**command line call**:


    elastix.exe [...] -fMask applicatorMask.ext -fmeshA1 applicatorMeshA.vtk -fmeshB1 applicatorMeshB.vtk -fmeshC1 applicatorMeshC.vtk [...]

###  Synthetic example

As an example a registration is set up with synthetic images that greatly simplifies a cervical brachy therapy image registration problem.

![alt-text](ScreenshotMSP.png)

See GitHub repo for the files of the setup and a movie that visualizes the registration process of the setup:

To mimic non-rigid deformations in the vicinity of the missing structure, that have impact on the final shape of the missing structure, the following static and moving objects were defined around the missing structure:

* brown ellipsoids represent the static structures, e.g. bones
* blue ellipsoid represents a moving structure in front of the 'missing structure', e.g. the bladder.
* purple ellipsoids represent moving structures behind the 'missing structure', e.g. the rectum.

The registration procedure is driven by the image data and the applicator mesh(es) only. The MissingStructurePenalty was configured to write deformed applicator meshes to disk each iteration. The deformed meshes of the surrounding structures are written to disk by the PolydataDummyPenalty each iteration and are used for visualization of the registration process.


###  Published in

The method and experiments are published in:

[1] F.F. Berendsen et al., Registration of structurally dissimilar images in MRI-based brachytherapy, Phys. Med. Biol. 59 (2014) 4033-4045.
