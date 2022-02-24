# Extracting top authors from csv file
pubmed <- read.csv("./Data/csv-fMRITitleA-set.csv")
authors <- pubmed$Authors
authors <- unlist(strsplit(authors, split  = ","))
autable <- as.data.frame(table(authors))
autable <- autable[order(autable$Freq,decreasing = TRUE),]
autable[1:20,]
write.csv(autable[1:20,],"./Data/top_authors.csv",row.names = FALSE)
