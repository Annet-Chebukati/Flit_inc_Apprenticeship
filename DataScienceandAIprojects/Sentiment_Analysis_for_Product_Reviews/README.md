# Sentiment Analysis for Product Reviews

## Overview
In this project, I conducted sentiment analysis on a collection of product reviews from an e-commerce platform. Utilizing a combination of text reviews and associated ratings, I developed a model capable of classifying the sentiment of each review as positive, negative, or neutral. The project leveraged natural language processing techniques and machine learning to analyze and categorize sentiments, providing valuable insights into customer feedback.

## Tools and Technologies
- **Python Libraries**: Utilized for data manipulation and analysis (Pandas, NLTK).
- **Machine Learning Libraries**: Employed for building and evaluating the sentiment analysis model (Scikit-learn, Spacy).
- **Jupyter Notebook**: The primary platform for documenting the analysis process.
- **GitHub**: Used for version control and sharing the project's codebase.
- **Streamlit**: Enabled the creation of an interactive web application to showcase the analysis results.

## Process and Methodology
1. **Data Preparation**: I began by importing the dataset into an SQL environment, ensuring the data was clean and structured for analysis.
2. **Exploratory Data Analysis (EDA)**: I conducted an initial exploration to understand the data's characteristics and identify any patterns.
3. **Data Preprocessing**: The text data was cleaned and preprocessed to ensure it was in the optimal format for modeling.
4. **Sentiment Labeling**: Each review was labeled according to its sentiment, derived from the text content and associated ratings.
5. **Text Vectorization**: I transformed the text data into a numerical format that machine learning models could interpret.
6. **Model Building**: A machine learning model was constructed to accurately classify the reviews' sentiment.
7. **Model Evaluation**: The model's performance was rigorously assessed using appropriate evaluation metrics.
8. **Sentiment Analysis Dashboard**: An interactive dashboard was created using Streamlit to visualize and interact with the sentiment analysis results.

## Key Deliverables
- A detailed [presentation]() or report summarizing the project's findings and recommendations.
- A comprehensive GitHub repository housing all documentation, [code](), and additional resources ([Jupyter Notebook](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/Sentiment%20Analysis.ipynb)) related to the project.
- An interactive dashboard was created using Streamlit to visualize and interact with the sentiment analysis results.

# Streamlit Sentiment Analysis Web App

This is a Streamlit web app for sentiment analysis on product reviews. The app uses a Random Forest Classifier to classify the sentiment of the reviews as either positive or negative.

## Code Overview

The [code](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/sentimentapp.py) for this app can be broken down into several parts:

1. **Data Loading and Preprocessing**: The app loads a dataset of product reviews and preprocesses the text data using techniques like cleaning, tokenization, and lemmatization.

2. **Model Training**: The app trains a Random Forest Classifier on the preprocessed data. The model is trained to predict whether a review is positive or negative. ![Model Score](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/model%20score.png)

3. **Web App Interface**: The app uses Streamlit to create a user-friendly web interface. Users can enter a review or upload a text file, and the app will use the trained model to predict the sentiment of the review.

## Running the App Locally

To run the app on your laptop using Anaconda Command Prompt(CMD.exe prompt), follow these steps:

1. **Download the streamlitapp.py file**: Download the streamlit.py file containing the code to your local machine.

2. **Open Anaconda Command Prompt**: Open the Anaconda Navigator Launch CMD.exe Prompt and navigate to the directory containing the code for example `cd Desktop\streamlit_app`.

3. **Install streamlit in your Environment**: If you haven't installed it yet you can do it by running `pip install streamlit` in your terminal.

.4 **Run the App**: Start the Streamlit server by running `streamlit run sentimentapp.py --client.showErrorDetails=false`. This will start the app and provide a URL to access it.

![App online view](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/Image3.png)

![App TXT file view](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/Image2.png)

## Testing the App

Once the app is running, you can test it by entering a review or uploading a text file containing a review. After you submit your input, the app will display the predicted sentiment of the review.

Here are some sample reviews you can use for testing:

![Positive Review](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/Image1.png)

![Negative Review](https://github.com/Annet-Chebukati/Flit_inc_Apprenticeship/blob/master/DataScienceandAIprojects/Sentiment_Analysis_for_Product_Reviews/Image4.png)

Remember, the app is just a tool and its predictions are not always 100% accurate. Always use your judgment when interpreting the results.


## Conclusion and Next Steps
The project successfully achieved its objective of classifying product review sentiments. The insights gained from this analysis can be leveraged to improve product offerings and customer experience. Future work may involve refining the model further and expanding the analysis to include a larger dataset or additional review platforms.

