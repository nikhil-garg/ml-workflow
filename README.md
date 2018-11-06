# Template / Workflow for Machine Learning tasks

This repository provides a suggestion for the code structure for Machine Learning projects and was worked out during a NLP project with Arag.

## Structure

```

│
├── Makefile                 <- Makefile with commands like `make data` or `make train`
│
├── README.md                <- The top-level README for developers using this project
│
├── environment.yml          <- The requirements file for reproducing the analysis environment, e.g.
│                                generated with `pip freeze > requirements.txt`
├── config-private.yml       <- config file in YAML, can be exported as env vars if need
│                                generated with `pip freeze > requirements.txt`
|
├── additional_models        <- additional models used for the project. E.g. language modules (corpora)
│
|
├── bin                      <- deleted stuff
│
|
├── data
│   ├── external             <- Data from third party sources.
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
│
|
├── documents
│   ├── docs
│   ├── images
│   └── references           <- Data dictionaries, manuals, and all other explanatory materials. Documentation
|
├── engine                   <- for Data Lake
│
|
├── kernel                   <- for Data Lake
│
|
├── misc                     <- miscellaneous
│
|
|
├── models                   <- folder with all the trained models
│
│
│
├── notebooks                <- Jupyter notebooks. Exploration is usually done here. A few templates on how to use
│     └── developper            implemented functions are provided.
|
|
├── reports                   <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures               <- Generated graphics and figures to be used in reporting
│
|
├── scores
│   └── model_name            <- Containes scores obtained by cross validation (automatically generated .csv file)
│        └── figures
│
│
├── src                       <- Source code for use in this project.
│   ├── __init__.py           <- Makes src a Python module
│   │
│   ├── data_extraction.py    <- Scripts to download or generate data
│   │ 
│   │
│   ├── helper_funcs          <- folder containing scripts
│   │   └── exploration.py    <- functions that help to explore and evaluate models. E.g. extended cross_validator
│   │   └── evaluation.py     <- Here functions for evaluations are implemented. (metrics, plot_confusion_matrix, 
│   │                            learning curves, auc_plot, show wrongly_classified data-points)      
│   │
│   ├── preprocessing.py      <- Scripts to preprocess the data and save them
│   │
|   └── programs.py           <- This is the place where the actual code is called.
```



# General Information (also NLP specific)
## How to install the code

### Special configuration to download the code from GitHub with git

In order to be able to install packages from an external GitHub server, we need to change the .gitconfig file which you can find in H:\.gitconfig. Change the file to:

```
[user]
	name = Vorname Nachname
	email = mail@axa-winterthur.ch
[https]
    proxy = https://C-Nummer:My_Password@sc-wvs-ch-win-pr-01-vip1.ch.doleni.net:8080
    sslVerify = false
[http]
    proxy = http://C-Nummer:My_Password@sc-wvs-ch-win-pr-01-vip1.ch.doleni.net:8080
    sslVerify = false
[http "https://github.axa.com"]
    proxy =
    sslVerify = false
[https "https://github.axa.com"]
    proxy =
    sslVerify = false
[credential "https://github.axa.com"]
    username = mail@axa-winterthur.ch
[credential]
    helper = wincred
[core]
    autocrlf = true
    filemode = false
```

Same for git, you need to create/change your pip.ini in C:\Users\CXXXXXX\pip

```
[list]
format=columns

[global]
trusted-host = github-production-release-asset-2e65be.s3.amazonaws.com 
proxy = https://C-Nummer:My_Password@sc-wvs-ch-win-pr-01-vip1.ch.doleni.net:8080
```

Unfortunately, you need to type in your Windows password. Also if your password contains special characters you need to encode them according to https://www.w3schools.com/tags/ref_urlencode.asp.

### Download the code from GitHub
- go to the directory in which you want to download the package from git  
- download the package from Github:   
  ```git clone https://github.axa.com/AXACH-CCDA/proj_claim_triage_arag.git```   
  or with other method from your choice (web interface, zip ...)   
- open an "Anaconda prompt" in the directory that contain the code from GitHub:   
  ```your_dir/your_project/```

### Create the python conda env  
This will provide you a unique list of python packages needed to run the code

- create a python env based on a list of packages from environment.yml    
  ```conda env create -f environment.yml -n env_your_proj```
  
 - activate the env  
  ```activate env_your_proj```
  
 - in case of issue clean all the cache in conda
   ```conda clean -a -y```

### Update or delete the python conda env 
- update a python env based on a list of packages from environment.yml  
  ```conda env update -f environment.yml -n env_your_proj```

- delete the env to recreate it when too many changes are done  
  ```conda env remove -n env_your_proj```


### Download the NLP configuration files (corpus ...)  

#### download the "Spacy" config files (corpus ...)
the files are now downloaded when creating the env but you needed to have a pip.ini file as explained above
 - de_core_news_sm-2.0.0.tar.gz
 - fr_core_news_sm-2.0.0.tar.gz
 - en_core_web_sm-2.0.0.tar.gz
 - it_core_news_sm-2.0.0.tar.gz

#### download the "Nltk" config files (corpus ...) option 1: make a local copy of the files
- copy the folder ```G:\GRP\BICCARB\99_NLP_Framework\nltk_data```
- in your user area: ```C:\Users\Cxxxxxx\AppData\Roaming```
- be careful, you don't see ```C:\Users\Cxxxxxx\AppData\Roaming``` but the folder exist 

#### download the "Nltk" config files (corpus ...) option 2: download the files directly
```python
>>> import nltk
>>> nltk.set_proxy('https://Cuser:PWD@sc-wvs-ch-win-pr-01-vip1.ch.doleni.net:8080')
>>> nltk.download()

in the pop-up windows choose "all"

or

>>> nltk.download() 
```


### Run the code
open an "Anaconda prompt" in the directory that contain the code from GitHub and execute:

EXAMPLE:

- to extract the data from the data:
   ```python main.py --program extract_data --mode prod```

- to do the full NLP processing based on the data extracted:    
   ```python main.py --program preprocess --mode prod```
   
