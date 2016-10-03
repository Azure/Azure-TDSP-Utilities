## Release Notes of TDSP Utilities
### Release date
09/27/2016
### What Have Been Released:

- Interactive Data Exploration, Analysis, and Reporting (IDEAR) in R: v0.1
- Automated Modeling and Reporting in R: v0.1

### Where to Get the Release
[IDEAR](https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils )

[Automated Modeling and Reporting](https://github.com/Azure/Azure-TDSP-Utilities/blob/master/DataScienceUtilities/Modeling)

### What Are New in this Release:

#### IDEAR:

- Support of data sources in local plain text files, and in SQL (including SQL Server, and SQL Data Warehouse).
- Support of data exploration for regression and classification tasks, based on the type of the target variable. Case is also supported if no target variable is specified in the YAML file, where the task is identified as data exploration. 
- Automatically detect the type of variables, if not specified in the YAML file.
- Print out the top k rows of the data, and the shape of the data.
- Generate the summary statistics of each variable.
- Investigate the distribution of each variable, and conduct normality test of each numerical variable.
- Rank numerical and categorical variables separately based on strength of association with the selected variable (default is the target variable).
- Box plot to show the relationship between a categorical variable and a numerical variable (ANOVA is used to test the strength of the relationship).
- Project high dimensional numerical matrix to 2-D and 3-D space spanned by principal components, to reveal the clustering pattern in the data. 
- Click a button to output the R script that generates the data exploration and visualization result to a log file specified in the YAML file.
- Click a Generate Report button to generate the report.
- Output new YAML file based on variable type detection result. This will be useful when in the beginning users do not know the variable types. In this way, the YAML files can evolve as users are getting more understanding to the data via the IDEAR exploration. 

#### Automated Modeling and Reporting

- Released [detailed markdown instruction](https://github.com/Azure/Azure-TDSP-Utilities/blob/master/DataScienceUtilities/Modeling/team-data-science-process-automated-modeling-reporting-instructions.md).
- Added detailed comments in the utility R script file
- Two sample data-sets are available at: https://github.com/Azure/Azure-TDSP-Utilities/tree/master/Data/Common: (i) UCI adult income (binary classification), and (iii) UCI bike rental/sharing (regression).


### Related Releases:

- [Team Data Science Process Overview and Instructions](https://github.com/Azure/Microsoft-TDSP)
- [Team Data Science Process Project Template](https://github.com/Azure/Azure-TDSP-ProjectTemplate)

### Other Resources:

We presented TDSP at Microsoft Data Science Summit on 9/27/2016: [Data Science Doesn’t Just Happen, It Takes a Process. Learn about Ours…](https://channel9.msdn.com/Events/Machine-Learning-and-Data-Sciences-Conference/Data-Science-Summit-2016/MSDSS23)
