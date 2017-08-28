installed_packages <- rownames(installed.packages())
# intall knitr 
if (!'knitr' %in% installed_packages){
  install.packages('knitr')
} else if ('1.15.1' != installed.packages()['knitr','Version']){
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
script.dir <- dirname(sys.frame(1)$ofile)
setwd(script.dir)
rmdfile = "IDEAR.rmd"
rmarkdown::run(rmdfile)