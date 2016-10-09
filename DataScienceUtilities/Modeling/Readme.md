# Product Information #
The **TDSP Automated Modeling and Reporting (AMR)** tool creates an automated workflow for generating and comparing multiple modeling approaches on a data-set.  

Currently available in R, it utilizes the Caret package to conveniently run multiple models on the data with a set of input parameters (which the users can specify through an yaml file). The accuracies of the models are then output for users to compare, and evaluate which modeling approach may be best for creating a final model for their predictive problem. Importance of the variables in the various models are also output for the users to examine which ones are important for model accuracy.

## Prerequisites ##
You must have the following installed on your machine:

> •	R 3.2.3 or newer version The Data Science VM on Azure has R 3.2.3 (Linux) or R 3.2.5 (Windows) installed for you by default. <br>
> •	RStudio

## How to run the AMR tool  ##
Details of how to run the AMR tool is provided [here](https://github.com/Azure/Azure-TDSP-Utilities/blob/master/DataScienceUtilities/Modeling/team-data-science-process-automated-modeling-reporting-instructions.md "here"). Briefly, you have to first specify your model parameters, as well as path to your data file in an yaml file. Then navigate to the directory of the which has the markdown file you want to run (currently there is one for binary classification and another one for regression), and initiate the run using the following one of the two following command: 

> o	Regression: rmarkdown::render("RegressionModelSelection.rmd")<br>
> o	Binary classification: rmarkdown::render("BinaryModelSelection.rmd")

This will prompt you provide the location of the yaml file, after which the run will progress to completion. The time taken for the run to complete will depend on various factors, such as, size of data-set, the number of cross-validation folds to run, number of parameters to sweep over, etc. 

After the run is finished, you will get an output HTML report, with accuracy of the models run, and variable importance information for each model. For details of the output, please see [this markdown file](https://github.com/Azure/Azure-TDSP-Utilities/blob/master/DataScienceUtilities/Modeling/team-data-science-process-automated-modeling-reporting-instructions.md "this markdown file").

## R packages ##
The following R packages are used in the AMR tool:
> glmnet<br>
> yaml<br>
> randomForest<br>
> xgboost<br>
> lattice<br>
> shiny<br>
> gridExtra<br>
> lme4<br>
> RODBC<br>
> pbkrtest<br>
> caret<br>

## Licensing ##
Use of the software is subject to acceptance of the [License Agreement](https://github.com/Azure/Azure-TDSP-Utilities/blob/master/DataScienceUtilities/Modeling/LICENSE.txt "Licence Agreement").
 

