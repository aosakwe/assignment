import pandas as pd
import glob
import os

# setting the path for joining multiple files
pattern = "./Data/Labeling/selected_papers_*.tsv"
files = os.path.join(pattern)

# list of files to merge
files = glob.glob(files)

# fout=open("./Data/Labeling/merged_annot.tsv","w",encoding='cp850')   
# for idx,file in enumerate(files):
# 	print(file)
# 	if idx == 0: #skips header for every subsequent file
# 		f = open(file,encoding='cp850')#.readlines()
# 	else:
# 		f = open(file,encoding='cp850').readlines()[1:]
# 	for idx,line in enumerate(f):
# 		if idx == 0:
# 			print(line)
# 		fout.write(line)
# fout.close()

# joining files with concat and read_csv
colnames = ['PMID', 'Title', 'Authors', 'Citation', 'First.Author', 'Journal.Book', 'Publication.Year', 'Create.Date', 'PMCID', 'NIHMS.ID', 'DOI', 'Data Available', 'Open Access', 'Code Available', 'Notes']
df = pd.concat(map(lambda fs: pd.read_csv(fs, sep='\t', names=colnames, header=0), files))
df.to_csv('./Data/Labeling/merged_annot.tsv', sep='\t', index=False)
