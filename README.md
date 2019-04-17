# proj_structure_code_workflow_ML
How to structure python code for some generic Machine Learning project with multiple developers?
That's the question we've asked oursevles and we tried to simplify the starting point of your project. Of course there is no single solution to this problem, and different projects require different workflows. Nonetheless, we tried to keep it general where possible. Furthermore, we've already implemented some functions that help you explore and validate your models.

This template is intended to be a starting point for larger machine learning projects such as Kaggle competitions worked on in a team. Feel free to adapt this template to your individual problems and drop parts that don't suit you or don't fit to your project.

We tried to come to a structure that helps you to avoid hard coding. This is the reason for the rather complicated starting point with a main.py file that calls function from programs.py. 

Lastly, we tried to optimize the structure for the use of git. .gitignore files are present and only need to be slightly adapted.

We hope we could help you with your project and in case of any question you can contact us under internal@analytics-club.org.


# Structure

```

├── LICENSE
│
│
├── README.md                <- The top-level README for developers using this project
│
├── environment.yml          <- Python environment
│                               
│
├── data
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
├── misc                     <- miscellaneous
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
│                               (if present)
│
├── scores                   <- Cross validation scores are saved here. (Automatically generated)
│   └── model_name           <- every model has its own folder. 
│
├── src                      <- Source code of this project. All final code comes here (Notebooks are thought for exploration)
│   ├── __init__.py          <- Makes src a Python module
│   ├── main.py              <- main file, that can be called.
│   │
│   │
│   └── utils                <- Scripts to create exploratory and results oriented visualizations
│       └── exploration.py      / functions to evaluate models
│       └── evaluation.py


# How to use a python environment
The purpose of virtual environments is to ensure that every developper has an identical python installation such that conflicts
due to different versions can be minimalized.

# Instruction
open a console and move to the folder where your environment file is stored.

## create a python env based on a list of packages from environment.yml
```conda env create -f environment.yml -n env_your_proj```

## update a python env based on a list of packages from environment.yml
```conda env update -f environment.yml -n env__your_proj```

## activate the env  
  ```activate env_your_proj```
  
## in case of an issue clean all the cache in conda
   ```conda clean -a -y```

## delete the env to recreate it when too many changes are done  
  ```conda env remove -n env_your_proj```

# How to use the template

 


# References
https://github.com/tarrade/proj_structure_code_workflow_ML

https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-2fa30d661c1e

https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-part-2-b5b420625102  

https://github.com/artofai/overcome-the-chaos

https://github.com/ThomasRobertFr/ml-project-structure

