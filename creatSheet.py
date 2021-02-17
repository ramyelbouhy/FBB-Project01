import streamlit as st
import pandas as pd
from loadData import loadoutput
import os
import matplotlib
matplotlib.use('Agg')

st.set_option('deprecation.showPyplotGlobalUse', False)


def creatSheet():
    st.title("Creat Daily Sheet")
    df = pd.DataFrame()
    df_mobile = pd.read_csv("C:/Users/ramye/Desktop/FBB-Project/Data/mobiles.csv")
    df_groups = pd.read_csv("C:/Users/ramye/Desktop/FBB-Project/groups.csv")
    df = loadoutput()
# __Change Columns type
    df_mobile['MSISDN'] = df_mobile['MSISDN'].astype('str')

# __Merge mobile to df
    if 'MSISDN' not in df.columns:
        pass
    else:
        df['MSISDN'] = df['MSISDN'].astype('str')
        df = df.merge(df_mobile, on='MSISDN', how='left')

# __Merge pop to df

    def mergePop():
        # appended pop list

        # usList = []
        popSer = []
        # get US from df and get first 5 No to irritae
        if 'UserName' not in df.columns:
            pass
        else:
            df['UserName'] = df['UserName'].astype('str')
            usList = df['UserName'].to_list()
            popList = []
            for us in usList:
                if us[:2] == ('04' or '06' or '07' or '08' or '09'):
                    popList.append('GOV')

                elif us[:2] == '03':
                    popList.append('Alx')

                elif us[:2] == '02':
                    popList.append('Cairo')
                    if us[:6] == '024220':
                        popList.append('sub Cairo_0')
                    elif us[:6] == '024221':
                        popList.append('sub Cairo_1')
                    elif us[:6] == '024222':
                        popList.append('sub Cairo_2')
                    elif us[:6] == '024223':
                        popList.append('sub Cairo_3')

                else:
                    popList.append('NA')

            popSer = pd.Series(popList)
        return popSer

    df['pop'] = pd.Series(mergePop())
    st.dataframe(df)
    # __Count of #SR
    st.write("Count of #SR")
    st.write((df.shape[0]) - 1)
    ag, pop = st.beta_columns(2)
    # __Agents Start
    if 'Owner' in df.columns:
        ag.write("Agents Start")
        ag.write(df.Owner.value_counts())
    # __POPs Start
        pop.write("POPs Start")
        pop.write(df['pop'].value_counts())
    # plot agent statrt
        vc_plot = df.groupby('Owner')['Owner'].count()
        st.write(vc_plot.plot(kind="bar"))
        st.pyplot()

    if st.button('export'):
        path = r"C:/Users/ramye/Desktop/"
        df.to_excel(os.path.join(path, r'green1.xlsx'), index=False)




