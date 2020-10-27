# Elastix Model Zoo
Welcome to the Model Zoo for parameter settings in Elastix, ITKElastix and SimpleElastix.
All models are displayed at https://elastix.lumc.nl/modelzoo, but static content including parameter files can be found here in the _models_ directory.

How to Upload Model Parameters
----------

- Fork ElastixModelZoo
- Add folder containing modelparameters.txt, readme.md, imagefiles.jpg (or .png/.jpeg) and/or jupyternotebook.ipynb to _models_ folder. (_Add File_ -> _Upload files_)
- Add commit message and _Commit changes_
- Create a _Pull Request_

Model Parameters folder
----------

The model parameters folder should contain at least:
- The parameter files in .txt format.
- A README.md which explains the context/study in which the parameter files where used, including the image content, image dimensionality and the image modality.
- The image files used in the readme in .png, .jpeg or .jpg format.

And optionally:
- A jupyter notebook file explaining the workflow in python (in case ITKElastix of SimpleElastix was used)
- example image data (try to limit the amount of large images)
- scripts or other files used in the study.

Github and Jupyter Notebook links will be generated automatically.
