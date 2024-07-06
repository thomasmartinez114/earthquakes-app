import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

    #graph plot
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=data['Depth'], y=data['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)