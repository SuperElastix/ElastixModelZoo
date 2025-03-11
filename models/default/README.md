# Default - elastix

This parameter file database entry contains "default" parameter files. These are intended for starting <tt>elastix</tt> users, and should give reasonable results in many applications. The <tt>elastix</tt> example (version 4.3 or higher), which can be downloaded from the [website](http://elastix.isi.uu.nl/download.php) contains the same parameter files, together with a test pair of images and an example script that calls <tt>elastix</tt>.

''Needless to say, it is virtually impossible to come up with default parameter values that give satisfactory results for every application. The parameter files provided here should rather be considered as a starting point.''

### Registration settings

<tt>elastix</tt> version: 4.3 and higher.

Example command line call:
<pre>
elastix -f fixed.mhd -m moving.mhd -p parameters_Rigid.txt -p parameters_BSpline.txt -out outputdir
</pre>

NB:
Up to elastix 4.5 the image dimensions had to be specified by the user.
<code>
   (FixedImageDimension 2)   -> (FixedImageDimension 3)
   (MovingImageDimension 2)  -> (MovingImageDimension 3)
</code>
From elastix 4.6, this is not necessary anymore.

NB2:
The files are saved in DOS text format. In order to use them on a Linux-based system, use the <tt>dos2unix</tt> tool to convert them to unix text format.

### Other comments

See the [elastix manual](https://github.com/SuperElastix/elastix/releases/download/5.2.0/elastix-5.2.0-manual.pdf) for an extensive introduction to <tt>elastix</tt> and explanation of many parameters. If you have any questions, please subscribe to the <tt>elastix</tt> mailing list and post your question there. We (the authors of <tt>elastix</tt>) are happy to answer any questions. Please do read the [FAQ](https://github.com/SuperElastix/elastix/wiki/FAQ) though ;)
