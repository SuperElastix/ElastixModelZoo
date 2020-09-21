
# Default0 - elastix

This parameter file database entry contains "default" parameter files. These are intended for starting `elastix` users, and should give reasonable results in many applications. The `elastix` example (version 4.3 or higher), which can be downloaded from the [website][1] contains the same parameter files, together with a test pair of images and an example script that calls `elastix`.

_Needless to say, it is virtually impossible to come up with default parameter values that give satisfactory results for every application. The parameter files provided here should rather be considered as a starting point._

###  Registration settings

`elastix` version: 4.3 and higher.

Example command line call:

    elastix -f fixed.mhd -m moving.mhd -p parameters_Rigid.txt -p parameters_BSpline.txt -out outputdir


NB: the parameter files are designed to work well both for 2D and 3D image registration. However, for 3D image registration you should first make the following change in each parameter file: ` `


      (FixedImageDimension 2)   -> (FixedImageDimension 3)
      (MovingImageDimension 2)  -> (MovingImageDimension 3)


NB2: the files are saved in DOS text format. In order to use them on a Linux-based system, use the `dos2unix` tool to convert them to unix text format.
Tags: 3D
###

See the elastix manual ([link][2]) for an extensive introduction to `elastix` and explanation of many parameters. If you have any questions, please subscribe to the `elastix` mailing list and post your question there. We (the authors of `elastix`) are happy to answer any questions. Please do read the [FAQ][3] though ;)

[1]: http://elastix.isi.uu.nl/download.php
[2]: http://elastix.isi.uu.nl
[3]: http://elastix.isi.uu.nl/FAQ.php
