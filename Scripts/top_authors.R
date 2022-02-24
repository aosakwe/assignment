# Extracting top authors from csv file
library(tidyverse)
pubmed <- read.csv("./Data/csv-fMRITitleA-set.csv")
authors <- pubmed$Authors
authors <- unlist(strsplit(authors, split  = ","))
authors <- sapply(authors, function(a) str_replace_all(a,"\\.",""))
autable <- as.data.frame(table(authors))
autable <- autable[order(autable$Freq,decreasing = TRUE),]
autable[1:20,]
write.csv(autable[1:20,],"./Data/top_authors.csv",row.names = FALSE)
