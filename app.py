import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header('Data Header')
    st.write(data.head())

def plot(dataframe):
    #graph plot
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=data['Depth'], y=data['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)


st.title('Earthquake Data Explorer')
st.text('This is a web app to explore earthquake data.')
#st.markdown('## This is **markdown**')

# set up sidebar
st.sidebar.title("Navigation")

uploaded_file = st.sidebar.file_uploader('Upload your file here')

options = st.sidebar.radio('Pages', options=['Home', 'Data Statistics', 'Data Header', 'Plot'])

# File uploader
if uploaded_file:
    # pandas to read the file
    data = pd.read_csv(uploaded_file)

# Render pages
if options == 'Data Statistics':
    stats(data)
elif options == 'Data Header':
    data_header(data)
elif options == 'Plot':
    plot(data)