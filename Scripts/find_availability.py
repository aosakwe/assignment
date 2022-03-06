#!/usr/bin/python3


## Python script to categorize articles by data/code availability

#Importing Tugce's script as a module
import pandas as pd
import pub_scraper as pub

#n_gram of phrases/words that could indicated data availability
n_gram = ["data availability","data available"]#,"code availability","data accessibility", "availability"]

pubmed = pd.read_csv("../Data/valid_papers.csv")
pubmed = pubmed.reset_index()

counts = []
doi = []
file_name = []

for index,row in pubmed.iterrows():
    count = pub.pub_wrapper(row['filename'],"data availability",n_gram)
    counts.append(count)
    doi.append(row['DOI'])
    file_name.append(row["filename"])
    #print(row["filename"] + " Score is: " + str(count))
output = pd.DataFrame({"DOI" : doi,"File" : file_name,"Score" : counts})
output.to_csv("../Data/pub_scraper_scores.csv")

