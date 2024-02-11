import streamlit as st
import pickle

import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()

    #tokenize
    text = nltk.word_tokenize(text)

    # remove special char
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    # remove stop words
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    # stemming
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
            
    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Spam Classifier")

input_sms = st.text_area("ENter message")

if st.button('Predict'):  

    # Preprocess

    transformed_sms = transform_text(input_sms)


    # vectorize

    vector_input = tfidf.transform([transformed_sms])

    # Prredict

    result = model.predict(vector_input)[0]

    # display

    if result == 1:
        st.header("SPammmmm")
    else:
        st.header("Safe msg")