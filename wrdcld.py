#!pip install wordcloud
#!pip install fileupload
#!pip install ipywidgets
#!jupyter nbextension install --py --user fileupload
#!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
#import fileupload
import io
import sys

tp = input()
hand = open(tp)
file_contents = hand.read()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''|!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "on", "for", "in", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    final_file_contents = ""
    for let in file_contents:
    	if let not in punctuations:
    		final_file_contents += let

    fc_list = final_file_contents.split()
    f_fc_list = []
    for wrd in fc_list:
    	if wrd.isalpha() and wrd not in uninteresting_words:
    		f_fc_list.append(wrd.lower())

    fc_dict = {}
    for wrd in f_fc_list:
    	if wrd in fc_dict:
    		fc_dict[wrd] += 1
    	else:
    		fc_dict[wrd] = 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(fc_dict)
    cloud.to_file("myfile.jpg")

calculate_frequencies(file_contents)

#myimage = calculate_frequencies(file_contents)
#plt.imshow(myimage, interpolation = 'nearest')
#plt.axis('off')
#plt.show()
#cloud = wordcloud.WordCloud()
#cloud.generate_from_frequencies(frequencies)
#cloud.to_file("myfile.jpg")