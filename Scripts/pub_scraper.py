#!/usr/bin/python3

## .py version of Tugce's web scraper python notebook
## can import this script as a module to use to parse through all the articles

# %%
#@markdown Install needed libraries
#pip install slate3k

# %%
#@markdown Import needed libraries
import re
import io
import requests
import slate3k as slate #Run above cell if it gives error for this library
import warnings


# %% [markdown]
# This part goes over following components:
# (1) **extractTextFromPDF(pdf_link)** - Extracting text from the PDF
# 
# (2) **findNumWords(extracted_text, target_word)** - Finding number of occurances of a target word in the extracted text
# %%
def extractTextFromPDF(pdf_link):
  '''
  Extracting text from the obtained article PDF url link
  ARGS:
    - pdf_link : (str) path to pdf in local storage
  RETURNS:
    - text : (str) text in the whole article
  '''
  ##Extract the text from PDF
  with open(pdf_link,'rb') as f:
    extracted_text = slate.PDF(f) #extract the text from the memory 
  ##Clean the text
  text = str(extracted_text) #convert to string for ease
  text = text.replace('\n', ' ') #replace \n with space
  text = text.replace('\\n', ' ') #replace \n with space

  return text

# %%
def findNumWords(extracted_text, target_word):
  '''
  Finds number of occurances of a target word in the extracted text
  ARGS:
    - extracted_text : (str) text extracted from the article PDF url link [comes from extractTextFromPDF()]
    - target_word : (str) the word we would like to search in the article
  RETURNS:
    - n : (int) number of occurances of the given target word in article
  '''
  word_list = re.findall(target_word, extracted_text, flags=re.IGNORECASE) #returns a list of the words that match with our target word
  n = len(word_list)
  #print(f'Number of occurances of the word {target_word} is {n}')
  return n

# %%
#An example of finding number of words in the text
# n0 = findNumWords(extracted_text, 'data')
# n1 = findNumWords(extracted_text, 'working memory')
# n2 = findNumWords(extracted_text, 'data avaliable')
def pub_wrapper(pdflink,target_word,n_gram):
  '''
  Wrapper function to run all functions built on a given link nd target word
  '''
  new_link = "../Paper_Dump/" + pdflink
  pdf_text = extractTextFromPDF(new_link)
  count = 0
  for word in n_gram:
    count += findNumWords(pdf_text, word)
  #count += findNumWords(pdf_text, target_word)
  return count #findNumWords(pdf_text, target_word)	

