import streamlit as st
import pandas as pd
import numpy as np


st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}")

age = st.slider("select your age:", 0,100,25)

st.write(f"your age is {age}")

options = ["python", "java", "c++", "c"]
choice = st.selectbox("choose your language:",options)
st.write(f"your chosen language is {choice}")


upload_file = st.file_uploader("Choose a CSV file", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df.head())



