repos.date <- "2017-08-01"
options(repos = c(CRAN = paste("https://mran.revolutionanalytics.com/snapshot/",
                               repos.date,sep="")))

installed_packages <- rownames(installed.packages())
# intall knitr 
if (!'knitr' %in% installed_packages){
  install.packages('knitr')
} else if ('1.16' != installed.packages()['knitr','Version']){
  remove.packages('knitr')
  install.packages('knitr')
}

if (!"rmarkdown" %in% installed_packages){
  install.packages("rmarkdown")
}

if (!"shiny" %in% installed_packages){
  install.packages("shiny")
}

library(rmarkdown)
library(tcltk)
library(tcltk2)

script.dir <- dirname(sys.frame(1)$ofile)
setwd(script.dir)
rmdfile = "IDEAR.rmd"
rmarkdown::run(rmdfile)