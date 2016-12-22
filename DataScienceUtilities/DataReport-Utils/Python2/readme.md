### Product Information

Interactive Data Exploratory Analysis and Reporting (IDEAR) is a tool developed for data scientists to interactively explore, visualize, and analyze data sets prior to building modeling tasks. This is a version of **Jupyter Notebook** that runs on _***Python 2.7***_. 

- Developed by Team Data Science Process (TDSP) team at Microsoft.
- Version: 0.1

### How to Run

The prerequisites are

- Jupyter Notebook with Python 2.7.
- The Jupyter Notebook server has been set up and is running on the machine that you have access. You should be able to clone the Azure-TDSP-Utilities repository to a directory on that machine. 

To start IDEAR in Jupyter Notebook running on Python 2.7, 

- Upload [IDEAR.ipynb](IDEAR.ipynb) to your Jupyter Notebook server.
- Set up the working directory as the directory on your Jupyter Notebook server machine where this readme.md file is located. 
- Provide the name and path of a YAML file. The path can be an absolute path or a relative path to the working directory on the Jupyter Notebook server. 
- Run cells in the Jupyter Notebook IDEAR.ipynb in order. 

For details, please read [instructions](team-data-science-process-idear-python-instructions.md).

### Python Modules 
The Python modules that are used in IDEAR are as follows. If your Jupyter Notebook server is running on Anaconda Python 2.7, most of the needed modules have been installed when you install Anaconda Python, with a few exceptions. However, if you are using [Azure Data Science Virtual Machines (DSVM)](https://azure.microsoft.com/en-us/marketplace/partners/microsoft-ads/standard-data-science-vm/), all modules are installed. 
 
- pandas
- numpy
- os
- [collections*](https://docs.python.org/2/library/collections.html)
- matplotlib
- [io*](https://docs.python.org/2/library/io.html)
- sys
- operator
- nbformat
- IPython
- ipywidgets
- scipy
- statsmodels
- [errno*](https://docs.python.org/2/library/errno.html)
- seaborn
- string
- functools

*Not included in Anaconda Python, but included in DSVM.

TDSP team from Microsoft also defined some functions to support IDEAR in Jupyter Notebook (Python 2.7). These functions are encapsulated in the following Python source code files. These files are in the same directory as this readme.md. 

- ReportMagics.py
- ConfUtility.py
- ReportGeneration.py
- UniVarAnalytics.py
- MultiVarAnalytics.py

### Licensing

Use of the software is subject to acceptance of the [License Agreement](../LICENSE.txt) 