import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1
    )

classifier = load_model()

def predict_sentiment(text):
    result = classifier(text)[0]
    return result["label"], result["score"]
