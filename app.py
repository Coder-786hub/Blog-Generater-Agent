from typing import Any
import streamlit as st
import pandas as pd
import mysql.connector
import google.generativeai as genai
from google.generativeai import types
from apikey import google_gemini_api

MODEL = "gemini-2.0-flash"
temperatur = 0.7
system_prompt = ""

genai.configure(api_key = google_gemini_api)
model = genai.GenerativeModel(MODEL,generation_config = types.GenerationConfig(temperature = temperatur))

# setting up our model



# set app to wide mode
st.set_page_config(layout = "wide")

# title of the our app 
st.title("❤️ Blog Generate AI Assistent : ❤️")

# create a subheader
st.subheader("Now you can craft perfect blogs with the help of Blog Generat AI Assistent")



# side bar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog You want to generate")
    
    # Blog title
    blog_title = st.text_input("Blog Title")

    # Keyword input
    keywords = st.text_area("Keywords (Comma-separated)")

    # Numbers of words
    num_words = st.slider("Number of words", min_value = 250, max_value = 1000, step = 250)

    # Number of images
    num_images = st.number_input("Number of images", min_value = 1, max_value = 5, step = 1)

    # submit button
    submit_btn = st.button("Generate Blog")

    # Prompts part
    prompt = f"""
            You are an expert blog writer. Write a detailed blog post based on the following information:

            Blog Title: {blog_title}

            Keywords: {keywords}

            Word Count: Approximately {num_words} words

            The blog should be:
            - Well-structured with headings and subheadings
            - Engaging and easy to read
            - SEO-friendly (use the keywords naturally throughout the blog)
            - Include suggestions for {num_images} relevant image descriptions or image topics

            Begin writing the blog below:
            """
    response = model.generate_content(contents = prompt)
    


if submit_btn:
    
    # st.image("https://en.wikipedia.org/wiki/Image#/media/File:Image_created_with_a_mobile_phone.png")
    st.write(response.text)    