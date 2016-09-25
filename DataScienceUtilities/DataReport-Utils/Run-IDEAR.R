installed_packages <- rownames(installed.packages())
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
