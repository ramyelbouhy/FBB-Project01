from loadDatam import *
from homePagem import *
from creatSheetm import creatSheet
from repPagem import *
import os
import streamlit as st
import pandas as pd


def homeP():
    homePageM()


def creatP():
    creatSheet()


def repP():
    repPage()


if __name__ == '__main__':
    sideSelect = st.sidebar.selectbox("FBB Phsical", ['Home', 'Creat Sheet', 'Rep'])
    if sideSelect == 'Home':
        homeP()
    elif sideSelect == 'Creat Sheet':
        creatP()
    elif sideSelect == 'Rep':
        repP()
    else:
        pass


