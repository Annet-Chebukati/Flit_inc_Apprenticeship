#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import re
import spacy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Suppress deprecation warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the data
@st.cache(allow_output_mutation=True)
def load_data():
    data_path = "https://raw.githubusercontent.com/Annet-Chebukati/Flit_inc_Apprenticeship/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/Amazon%20Product%20Review.txt"
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

# Train the model
@st.cache(allow_output_mutation=True)
def train_model(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    fit_model = clf.fit(X_train, y_train)
    return fit_model

fit_model = train_model(X_train, y_train)
y_pred = fit_model.predict(X_test)

def run():
    st.title('Sentiment Analysis for Product Reviews')
    st.header('This app uses a Random Forest Classifier to classify the sentiment of Amazon Product Reviews.')
    # Include the model results here
    st.write('Training accuracy:', fit_model.score(X_train, y_train))
    st.write('Test accuracy:', fit_model.score(X_test, y_test))
    st.write('AUC-ROC:', roc_auc_score(y_test, y_pred))
    st.text('Classification Report:')
    st.text(classification_report(y_test, y_pred))
    st.text('Confusion Matrix:')
    st.text(confusion_matrix(y_test, y_pred))
    
    add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online", "Txt file"))
    if add_selectbox == "Online":
        user_input = st.text_area('Enter your review')
        if st.button("Predict"):
            # Vectorize the user's input
            user_input_vectorized = vectorizer.transform([user_input])
            # Predict the sentiment of the user's input
            prediction = fit_model.predict(user_input_vectorized)
            # Display the prediction with a matching emoji
            if prediction == 0:
                st.error('Negative sentiment 😞')
            else:
                st.success('Positive sentiment 😄')
    elif add_selectbox == "Txt file":
        file_buffer = st.file_uploader("Upload text file for new item", type=["txt"])
        if st.button("Predict"):
            text_news = file_buffer.read()
            # Vectorize the user's input
            user_input_vectorized = vectorizer.transform([text_news])
            # Predict the sentiment of the user's input
            prediction = fit_model.predict(user_input_vectorized)
            # Display the prediction with a matching emoji
            if prediction == 0:
                st.error('Negative sentiment 😞')
            else:
                st.success('Positive sentiment 😄')

if __name__ == "__main__":
    run()

