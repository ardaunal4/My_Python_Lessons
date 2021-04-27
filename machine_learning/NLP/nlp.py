# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:36:47 2021

@author: ardau
"""
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\\Users\\ardau\\OneDrive\\Masaüstü\\machine_learning\\NLP\\gender_classifier.csv", encoding = "latin1")

data = pd.concat([df.gender, df.description], axis = 1)

data.dropna(axis = 0, inplace = True)

data.gender = [1 if each  == "female" else 0 for each in data.gender]

#%% Clean Data

import re

first_description = data.description[4]
description = re.sub("[^a-zA-Z]", " ", first_description) # '^' means that not. This line of code means that 
# if there are letters different than a-zA-Z(alphabet), change them with space(" ").
description = description.lower() # make all letters lower

#%% Implement stop words (irrelivant words

import nltk # Natural Language Tool Kit
nltk.download("stopwords") # download stopwords with internet
from nltk.corpus import stopwords # import dowloaded stopwords into code

# There is a better way to split words in NLTK library which is better the .split() method. 
# It splits also conconated words such as isn't as is not
description = nltk.word_tokenize(description, language = "english")

# Remove unnecessary words from data
description = [word for word in description if word not in set(stopwords.words("english"))]

#%% Lemmatazation is a method which founds root of the words. For ex: ate -> eat, sleeps -> sleep

import nltk as nlp

lemma = nlp.WordNetLemmatizer()
description = [lemma.lemmatize(word) for word in description] 

description = " ".join(description)

#%% Generalization of hole logic with dataset intead of one word

description_list = []

for description in data.description:
    
    description = re.sub("[^a-zA-Z]", " ", description)
    description = description.lower()   
    description = nltk.word_tokenize(description)
    description = [word for word in description if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    description = [lemma.lemmatize(word) for word in description]
    description = " ".join(description)
    description_list.append(description)
    
#%% Create Bag of Words

from sklearn.feature_extraction.text import CountVectorizer # Method for creation of bag of words 

count_vectorizer = CountVectorizer(max_features = 500, stop_words = "english") # max_features is the number of words in the bag
sparce_matrix = count_vectorizer.fit_transform(description_list).toarray() 

print("Most frequently used {} words: {}".format(500, count_vectorizer.get_feature_names()))


#%% Prepare data for machine learning model

y = data.iloc[:,0].values   # male or female classes
x = sparce_matrix
# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)  

# %% Naive Bayes ML Model

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)

#%% prediction

y_pred = nb.predict(x_test)
print("Accuracy: ", nb.score(y_pred.reshape(-1, 1), y_test))  
    
    
    
