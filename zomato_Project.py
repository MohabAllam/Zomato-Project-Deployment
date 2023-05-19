
import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Create Sidebar to navigate between pages
sidebar = st.sidebar
mode = sidebar.radio('Mode', ['EDA'])
st.markdown("<h1 style='text-align: center; color: #ff0000;'></h1>", unsafe_allow_html=True)

# Header of Customer Satisfaction Prediction
html_temp="""
            <div style="background-color:#F5F5F5">
            <h1 style="color:#31333F;text-align:center;"> Exploratory Data Analysis </h1>
            </div>
        """
st.markdown(html_temp, unsafe_allow_html= True)

if mode == "EDA":

    def main():
        # Create sidebar to upload CSV files
        with st.sidebar.header('Upload your CSV data'):
            uploaded_file = st.sidebar.file_uploader('Upload your input csv file')

        if uploaded_file is not None:
            # Read file and Put headers
            EDA_sample = pd.read_csv(uploaded_file, index_col= 0)
            pr = ProfileReport(EDA_sample, explorative=True)
            st.header('**Input DataFrame**')
            st.write(EDA_sample)
            st.write('---')
            st.header('**Pandas Profiling Report**')
            st_profile_report(pr)
        
        else:
            st.info('Awaiting for CSV file to be uploaded.')

    if __name__ == '__main__':
        main()
