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
# __C:/Users/ramye/Desktop/FBB-Project/
def loadGroups(folder_path='\\mob-fs-01.mobcorp.intrt.com\\FBB Technical support\\Data'):
    group_df = pd.DataFrame()
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select Groups Sheet", filenames)
    if selected_filename is not None:
        group_df = pd.read_csv(selected_filename)
    return group_df


 # __test vlookup on poplist


def testpop():
    data = pd.DataFrame()
    # __ r'C:/Users/ramye/Desktop/FBB-Project/data/pop.xlsx'
    path = r'\\mob-fs-01.mobcorp.intrt.com\\FBB Technical support\\Data\\pop.xlsx'
    if path is not None:
        xls = pd.ExcelFile(path)
        data = pd.read_excel(xls)
        teplist = []
        data['code1'] = data['code1'].astype('str')
        for x in data['code1']:
            teplist.append("0"+x)
        data['code1'] = pd.Series(teplist)
    return data






