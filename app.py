import streamlit as st
import pandas as pd

st.title('Earthquake Data Explorer')
st.text('This is a web app to explore earthquake data.')
#st.markdown('## This is **markdown**')

uploaded_file = st.file_uploader('Upload your file here')

if uploaded_file:

    st.header("Data Statistics")
    # pandas to read the file
    data = pd.read_csv(uploaded_file)

    # display the information
    st.write(data.describe())

    st.header('Data Header')
    st.write(data.head())