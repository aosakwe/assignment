#!/usr/bin/python3


## Python script to categorize articles by data/code availability

#Importing Tugce's script as a module
import pandas as pd
import numpy as np
import pub_scraper as pub

#n_gram of phrases/words that could indicated data availability
n_gram = ["data availability","data available"]#,"code availability","data accessibility", "availability"]

pubmed = pd.read_csv("../Data/valid_papers.csv")
pubmed = pubmed.reset_index()
for index,row in pubmed.iterrows():
    count = pub.pub_wrapper(row['filename'],"data availability",n_gram)
    print(row["filename"] + " Score is: " + str(count))
