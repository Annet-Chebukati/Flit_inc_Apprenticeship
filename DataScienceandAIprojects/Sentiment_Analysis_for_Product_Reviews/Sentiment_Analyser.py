# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

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

# Apply the NLTK tokenization to reviews
amz_df['reviews_text'] = amz_df['review_body'].apply(lambda row: ' '.join([word for word in word_tokenize(row)]))

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
st.title('Sentiment Analysis for Product Reviews')
st.write('This app uses a Random Forest Classifier to classify the sentiment of Amazon Product Reviews.')
st.write(
    'To explore the Amazon Product Review data, please check out my Github. To see my source code, have a look at my GitHub repo.')
st.write('*Note: it will take up a few seconds to run the app.*')
st.write('Training accuracy:', fit_model.score(X_train, y_train))
st.write('Test accuracy:', fit_model.score(X_test, y_test))
st.write('AUC-ROC:', roc_auc_score(y_test, y_pred))
st.text('Classification Report:')
st.text(classification_report(y_test, y_pred))
st.text('Confusion Matrix:')
st.text(confusion_matrix(y_test, y_pred))

# Create a form for user input
form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your review')
submit = form.form_submit_button('Submit')
# Process the user input when the form is submitted
if submit:
    # Vectorize the user's input
    user_input_vectorized = vectorizer.transform([user_input])

    # Predict the sentiment of the user's input
    prediction = clf.predict(user_input_vectorized)

    # Display the prediction with a matching emoji
    if prediction == 0:
        st.error('Negative sentiment 😞')
    else:
        st.success('Positive sentiment 😄')

