import streamlit as st
import os
import pandas as pd


# __Upload Mobile Sheet (csv)
def loadMobile(folder_path='C:/Users/ramye/Desktop/FBB-Project/'):
    mobile_df = pd.DataFrame()
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select Mobiles Sheet", filenames)
    if selected_filename is not None:
        mobile_df = pd.read_csv(selected_filename)
    return mobile_df


# __Upload Groups file (csv)
def loadGroups(folder_path='C:/Users/ramye/Desktop/FBB-Project/'):
    group_df = pd.DataFrame()
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select Groups Sheet", filenames)
    if selected_filename is not None:
        group_df = pd.read_csv(selected_filename)
    return group_df


# __Upload output file (csv)
def loadoutput():
    data = pd.DataFrame()
    uploadFile = st.file_uploader("Choose output.csv file", type=['csv'])
    if uploadFile is not None:
        df = pd.read_csv(uploadFile)
        data = df
    return data
