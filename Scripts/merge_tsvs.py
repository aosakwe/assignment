import pandas as pd
import glob
import os

# setting the path for joining multiple files
pattern = "./Data/Labeling/selected_papers_*.tsv"
files = os.path.join(pattern)

# list of files to merge
files = glob.glob(files)

fout=open("./Data/Labeling/merged_annot.tsv","a",encoding='cp850')   
for idx,file in enumerate(files):
	print(file)
	if idx == 0: #skips header for every subsequent file
		f = open(file,encoding='cp850')#.readlines()
	else:
		f = open(file,encoding='cp850').readlines()[1:]
	for idx,line in enumerate(f):
		fout.write(line)
fout.close()

# joining files with concat and read_csv
#issue : gives NaN type for the annotation columns
# df = pd.concat(map(lambda fs: pd.read_csv(fs, sep='\t'), files))
# print(df)