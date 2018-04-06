
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os
from sklearn import svm, model_selection, tree, preprocessing, metrics
from sklearn.ensemble import RandomForestClassifier
import codecs
from nltk.probability import FreqDist
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
import helper
import scipy.special as sp
import random


path='/mnt/A042994142991CDA/Hindi_train/'
svm_scores=[]
random_forest_scores=[]
svm_times=[]
random_forest_times=[]


vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2,2), min_df = 0)

for i in range(3,15):
    iterations=0
    x=int(sp.comb(14,i))
    if(x>20):
        iterations=20
    else:
        iterations=x
    
    x1=0
    x2=0
    y1=0
    y2=0
    for a in range(iterations):
        random_list=random.sample(range(14),i)
        train_data_X,train_data_Y,length=helper.prepare_data(authors_to_consider=random_list,vectorizer=vectorizer,add_features='no',path=path,no_of_authors=i)

    
        helper.text_normalise(train_data_X,length)  #tf-idf normalisation
        helper.feature_normalise(train_data_X)      #normalisation for machine learning algo

        a,b,c,d=helper.learn(train_data_X,train_data_Y)
        x1+=a
        x2+=b
        y1+=c
        y2+=d
        
    x1=x1/iterations
    x2=x2/iterations
    y1=y1/iterations
    y2=y2/iterations
    
    svm_scores+=[x1]
    svm_times+=[x2]
    random_forest_scores+=[y1]
    random_forest_times+=[y2]
    















# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot([x for x in range(3,15)],svm_scores)


# In[7]:


plt.plot([x for x in range(3,15)],random_forest_scores)


# In[8]:


plt.plot([x for x in range(3,15)],svm_times)


# In[9]:


plt.plot([x for x in range(3,15)],random_forest_times)


# In[5]:


plt.show()

