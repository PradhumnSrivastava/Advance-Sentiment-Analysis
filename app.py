import streamlit as st
from model import predict_sentiment

st.set_page_config(page_title="Sentiment Analyzer")

st.title("Sentiment Analysis App")

st.write("Enter text to analyze sentiment.")

user_input = st.text_area("Enter text here:")

if st.button("Predict"):
    if user_input.strip() != "":
        label, score = predict_sentiment(user_input)

        if label == "POSITIVE":
            st.success(f"Sentiment: {label}")
        else:
            st.error(f"Sentiment: {label}")

        st.write("Confidence Score:", round(score, 3))
    else:
        st.warning("Please enter text.")
