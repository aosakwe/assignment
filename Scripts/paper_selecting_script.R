## Script from Benjamin Rudski ##
library(stringr)
library(purrr)
library(dplyr)

s = "IDS FROM SLACK"
indices = str_split(s, "\\s+")
indices <- map(indices, as.integer)
indices <- c(indices, recursive = TRUE)
papers <- read.csv("./Data/csv-fMRITitleA-set.csv", header = T)
papers %>% slice(indices) -> selected.papers
write.table(selected.papers, "./Data/selected_papers.csv", sep="\t", row.names=FALSE)
