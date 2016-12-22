**Date of release**

* 12/31/2016

**Content of release**

* Interactive Data Exploration, Analysis, and Reporting (IDEAR) in R
* Interactive Data Exploration, Analysis, and Reporting (IDEAR) in Jupyter Notebooks (Python 2.7)

**Released version**

* 0.11

**Where to get the release**

* [https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils](https://github.com/Azure/Azure-TDSP-Utilities )

**New features**

* IDEAR in Jupyter Notebooks (Python 2.7). Python users can get interactive data exploration, analysis, visualization, and reporting capabilities similar to IDEAR in R. 
* Automatic datetime fields featurization in IDEAR in R. This feature extract datetime components automatically from user-specified datetime columns, such as year, month, day, day of week etc. The extracted datetime component columns are added to the right of the original dataset for analysis and explore. If the data source is local file, the augmented dataset is automatically saved in the same directory of the original data file. 
* In IDEAR in R, visualize categorical variables in respect of factor in barplot
* In IDEAR in R, sort categorical variables by factor frequency in piechart

**Enhanced features**

* Updated the generated html report file path to make it work in R Tools for Visual Studio (RTVS)
* Unified coding style in IDEAR in R.

**Related releases**

* TDSP Project Template:
[https://github.com/Azure/Azure-TDSP-ProjectTemplate](https://github.com/Azure/Azure-TDSP-ProjectTemplate)
* TDSP Instructions:
[https://github.com/Azure/Microsoft-TDSP](https://github.com/Azure/Azure-TDSP-ProjectTemplate)
* TDSP AMAR Utilities 
[https://github.com/Azure/Azure-TDSP-Utilities/blob/master/DataScienceUtilities/Modeling](https://github.com/Azure/Azure-TDSP-ProjectTemplate)