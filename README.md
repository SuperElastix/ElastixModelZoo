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

A template model folder can be found under models/template.
The template should be followed to ensure that the links on the model zoo website and the references in the overview table are correctly generated.

The model parameters folder should contain at least:
- The parameter files in .txt format.
- A README.md which explains the context/study in which the parameter files where used, including the image content, image dimensionality and the image modality.
- The image files used in the README in .png, .jpeg or .jpg format.

And optionally:
- A jupyter notebook file explaining the workflow in python (in case ITKElastix of SimpleElastix was used).
- example image data (try to limit the amount of large images)
- scripts or other files used in the study.

The README.md style should be consistent with the other README.md files and should contain caption like '###  Registration settings'.
The link to the correct GitHub folder will be automatically appended after the '###  Registration settings' caption or at the end if this caption is absent.
A Jupyter Notebook link will also be generated automatically.
