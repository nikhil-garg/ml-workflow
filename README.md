# proj_structure_code_workflow_ML
How to structure python code some some generic ML project. The idea is to have a generic template with an automatic workflow.

This template is intended to be a starting point in larger ML projects such as Kaggle Competition worked on in a team.
If you've never worked on a large project involving several developpers you probably ask yourself:
"Why should I use such a complicated structure?!"
We agree that the following structure is not the simplest and that it could be done in an easier way. Our intention
is to provide a template that suits most ML problems and can be applied to quite large projects of any kind. Feel free to
adapt this template to your individual problem and drop parts that don't suit you.
The template is made in a from such that hard-coding is avoided. This is we implemented the template such that you need to call
the main and passing an argument. The argument specifies what code will be called in the program. It allows you to start on one single
code from beginning on without always executing the whole code. Furthermore, several developpers may work on different tasks within the
same code simultaneously.
Lastly, we tried to optimize the structure for the use of git. .gitignore files are present and only need to be slightly adapted.

We hope we could help you with your project and in case of any question you can contact us under internal@analytics-club.org.


# Structure

```

├── LICENSE
│
│
├── README.md                <- The top-level README for developers using this project
│
├── environment.yml          <- The requirements file for reproducing the analysis environment, e.g.
│                                generated with `pip freeze > requirements.txt`
│
├── additional_models        <- Folder for additional models, e.g. Language models from Spacy, nltk,...
│
│
├── bin                      <- Stuff to be deleted
│
│
├── data
│   ├── external             <- Data from third party sources.
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
│
│
├── documents                <- Documentation of data etc.
│   ├── docs
│   ├── images
│   └── references           <- Data dictionaries, manuals, and all other explanatory materials.
│
│
├── misc                      <- miscellaneous
│
│
├── notebooks                <- Jupyter notebooks. Every developper has its own folder for exploratory
│   ├── name                    notebooks. Usually every model has its own notebook where models are
│   │   └── exploration.ipynb   tested and optimized.
│   └── model
│       └── model_exploration.ipynb <- different optimized models can be compared here if preferred    
│
│
├── reports                   <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures               <- Generated graphics and figures to be used in reporting
│
│
├── results
│   ├── outputs
│   └── models               <- Trained and serialized models, model predictions, or model summaries
│
│
├── scores                   <- Cross validation scores are saved here. (Automatically generated)
│   └── model_name           <- every model has its own folder. 
│
├── src                      <- Source code for use in this project.
│   ├── __init__.py          <- Makes src a Python module
│   ├── programs.py          <- main calls a function from programs. These functions represent different steps
│   │                           within the workflow.
│   ├── data                 <- Scripts to download or generate data
│   │   └── data_extraction.py
│   │
│   ├── process              <- Scripts to turn raw data into features for modeling
│   │   └── processing.py
│   │
│   │
│   └── utils                <- Scripts to create exploratory and results oriented visualizations
│       └── exploration.py      / functions to evaluate models
│       └── evaluation.py

```

# Instruction
## create a python env based on a list of packages from environment.yml
```conda env create -f environment.yml -n env_ds```

## update a python env based on a list of packages from environment.yml
```conda env update -f environment.yml -n env_ds```

## download the data manually
python src/data/download.py "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" data/raw/iris.csv


# References
https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-2fa30d661c1e

https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-part-2-b5b420625102  

https://github.com/artofai/overcome-the-chaos

https://github.com/ThomasRobertFr/ml-project-structure

# Makefile documentation

There are seven “core” automatic variables:

    $@: The filename representing the target.

    $%: The filename element of an archive member specification.

    $<: The filename of the first prerequisite.

    $?: The names of all prerequisites that are newer than the target, separated by spaces.

    $^: The filenames of all the prerequisites, separated by spaces. This list has duplicate filenames removed since for most uses, such as compiling, copying, etc., duplicates are not wanted.

    $+: Similar to $^, this is the names of all the prerequisites separated by spaces, except that $+ includes duplicates. This variable was created for specific situations such as arguments to linkers where duplicate values have meaning.

    $*: The stem of the target filename. A stem is typically a filename without its suffix. Its use outside of pattern rules is discouraged.

https://stackoverflow.com/questions/3220277/what-do-the-makefile-symbols-and-mean

