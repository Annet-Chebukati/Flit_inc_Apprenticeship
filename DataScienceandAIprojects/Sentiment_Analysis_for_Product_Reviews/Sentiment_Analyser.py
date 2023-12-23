#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Set the style for plots
plt.style.use('ggplot')

# Load the data
@st.cache
def load_data():
    data_path = "C:\\ANITA CHEBUKATI\\FLIT\\Sentiment Analysis for Product Review\\Amazon Product Review.txt"
    amz_df = pd.read_csv(data_path)
    return amz_df

amz_df = load_data()

# Clean the text
def clean_text(Review):
    Review = str(Review).lower()  # convert to lowercase
    Review = re.sub('\[.*?\]', '', Review)
    Review = re.sub('https?://\S+|www\.\S+', '', Review)  # Remove URLs
    Review = re.sub('<.*?>+', '', Review)
    Review = re.sub(r'[^a-z0-9\s]', '', Review)  # Remove punctuation
    Review = re.sub('\n', '', Review)
    Review = re.sub('\w*\d\w*', '', Review)
    return Review

amz_df['review_body'] = amz_df['review_body'].apply(clean_text)

# Load the English model for spaCy
nlp = spacy.load('en_core_web_sm')

# Apply the spaCy pipeline to reviews
amz_df['reviews_text'] = amz_df['review_body'].apply(lambda row: ' '.join([token.lemma_ for token in nlp(row) if not token.is_stop]))

# Define the resampling method
method = SMOTE(random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(amz_df['reviews_text'])

# Create the resampled feature set
X_resampled, y_resampled = method.fit_resample(X, amz_df['sentiment'])

# Split your resampled data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, random_state=42, test_size=0.20)

# model
clf = RandomForestClassifier(n_estimators=100, random_state=42)

fit_model = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Streamlit code to display results
st.title('Sentiment Analysis Model Results')
st.write('Training accuracy:', fit_model.score(X_train, y_train))
st.write('Test accuracy:', fit_model.score(X_test, y_test))
st.write('AUC-ROC:', roc_auc_score(y_test, y_pred))
st.text('Classification Report:')
st.text(classification_report(y_test, y_pred))
st.text('Confusion Matrix:')
st.text(confusion_matrix(y_test, y_pred))

