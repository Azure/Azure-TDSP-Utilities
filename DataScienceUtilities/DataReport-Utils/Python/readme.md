### Product Information

Interactive Data Exploratory Analysis and Reporting (IDEAR) is a tool developed for data scientists to interactively explore, visualize, and analyze data sets, and get insights to the data sets. The Python version of IDEAR is delivered through Jupyter Notebooks which can run on both ***Jupyter Notebook Server*** that you have and any notebook services in Python 2.7 or 3.5 kernel, as long as the required Python libraries are installed on the notebook server.  

- Developed by Team Data Science Process (TDSP) team at Microsoft.
- Version: 0.12

### How to Run

The prerequisites to run IDEAR in Jupyter Notebooks (Python 2.7 or 3.5) are:

- Jupyter Notebook with Python (2.7 or 3.5).
- The Jupyter Notebook server has been set up and is running on the machine that you have access. You should be able to clone the Azure-TDSP-Utilities repository to a directory on that machine. 

If you are running IDEAR Python in Azure Notebooks, you need to have:

- Azure subscription and access to Azure Notebooks account
- Azure Blob storage account and be able to upload data to Azure blobs

To start IDEAR in Jupyter Notebook running on Python (2.7 or 3.5), 

- Upload [IDEAR.ipynb](IDEAR.ipynb) to your Jupyter Notebook server.
- Set up the working directory as the directory on your Jupyter Notebook server machine where this readme.md file is located. 
- Provide the name and path of a YAML file. The path can be an absolute path or a relative path to the working directory on the Jupyter Notebook server. 
- Run cells in the Jupyter Notebook IDEAR.ipynb in order. 

To start IDEAR in Azure Notebooks:

- Upload data and yaml file into your Azure Blob storage
- Log in to Azure Notebooks account
- Upload [IDEAR-Python-AzureNotebooks.ipynb](IDEAR-Python-AzureNotebooks.ipynb) to your library
- Type in the Azure Blob storage credentials when prompt

For details, please read [instructions](IDEAR-Python-Instructions-JupyterNotebook.md).

### Python Modules

The Python modules that are used in IDEAR are as follows. If your Jupyter Notebook server is running on Anaconda Python (2.7 or 3.5), most of the needed modules have been installed when you install Anaconda Python, with a few exceptions. However, if you are using [Azure Data Science Virtual Machines (DSVM)](https://azure.microsoft.com/en-us/marketplace/partners/microsoft-ads/standard-data-science-vm/), all modules are installed.

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
- pyyaml
- scikit-learn

*Not included in Anaconda Python, but included in DSVM.

See the next section and the `idear_env.yml` file for specific versions of additional installs.

### Conda environment

The `idear_env.yml` provides a mechanism for creating a reproducible environment for running this tool. It requires that some version of the `conda` tool is installed (testing was done on Windows 10 machine with conda 4.3.30). You can create the conda environment by running a command prompt with access to conda in it and running:

```
cd PATH/TO/THIS/README/FILE
conda env create -f idear_env.yml
```

In order to execute the `IDEAR.ipynb` notebook against this, you will need to either:

- (RECOMMENDED): [Install the nb_conda_kernels package](https://github.com/Anaconda-Platform/nb_conda_kernels) to the environment in which you are launching jupyter. Once you open the notebook with the conda environment created, you can then just set that environment as the appropriate kernel for execution.
- Alternatively, you can run jupyter from the conda environment created (the instructions vary slightly for bash vs. powershell). However, it's a good idea to run `jupyter nbextension enable --py –sys-prefix widgetsnbextension` from this environment prior to starting the notebook server.

For PowerShell:

```
conda activate idear_env
```

For Bash:

```
source activate idear_env
```

Then, in either shell, 

```
jupyter nbextension enable --py –sys-prefix widgetsnbextension
jupyter notebook
```

**NOTE** There are likely to be some warnings around different versions of Javascript that result from this environment, particularly if you leverage it in the RECOMMENDED approach above.

### Support Functions

TDSP team from Microsoft also defined some functions to support IDEAR in Jupyter Notebook (Python 2.7 and 3.5). These functions are encapsulated in the following Python source code files. These files are in the same directory as this readme.md. 

- ReportMagics.py
- ConfUtility.py
- ReportGeneration.py
- UniVarAnalytics.py
- MultiVarAnalytics.py

### Licensing

Use of the software is subject to acceptance of the [License Agreement](../LICENSE.txt) 
