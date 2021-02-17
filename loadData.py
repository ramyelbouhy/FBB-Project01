import streamlit as st
import os
import pandas as pd
from os import listdir
from os.path import isfile, join
from pathlib import Path
import csv


# __Upload output file (csv)
def loadoutput():
    data = pd.DataFrame()
    uploadFile = st.file_uploader("Choose ('xlsx' or 'xls') file", type=['xlsx', 'xls'])
    if uploadFile is not None:
        xls = pd.ExcelFile(uploadFile)
        df = pd.read_excel(xls)
        data = df
    return data


# __Upload Mobile Sheet (csv)


def loadMobile():
    pass


# __Upload Groups file (csv)
def loadGroups(folder_path='C:/Users/ramye/Desktop/FBB-Project/'):
    group_df = pd.DataFrame()
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select Groups Sheet", filenames)
    if selected_filename is not None:
        group_df = pd.read_csv(selected_filename)
    return group_df






