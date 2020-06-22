############################################
# Chapter 1: Language Processing and Python


################# Import Libraries
import nltk
# nltk.download()
from nltk.book import *

# shows us every occurrance of a word
text1.concordance('monstrous')

# other words that appear in similar range of contexts
text1.similar('monstrous')

# contexts that are shared by words
text2.common_contexts(["monstrous","very"])

# location of words in text
text4.dispersion_plot(["citizens","democracy","freedom","duties", "America"])

# generate randome text
text1.generate()

# number of words in text
len(text3)

# count of occurrances for specific word
text3.count("smote")

# distinct tokens in text (include punctuation)
set(text3)
len(set(text3))

# average num times words used per text
def lexical_diversity(text):
    return len(text)/len(set(text))

# pct occurrance within text (count = text1.count("word"), total = len(text1))
def percentage(count, total):
    return 100 * count / total
