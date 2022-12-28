import numpy as np
import pandas as pd
import streamlit as st


import os
list_file = os.listdir()
file = [x for x in list_file if(x[-3:] == 'csv')]
st.title('App per i parcometri di roma')
df_parcometri = pd.read_csv(file[0], sep=';')
df_parcometri

zona = df_parcometri.Ambito.value_counts()
st.subheader('visualizza il numero di parcometri in base alla zona')
st.bar_chart(zona)

df_parcometri.rename(columns={'Latitude' : 'latitude'}, inplace= True)

df_parcometri.rename(columns={'Longitude' : 'longitude'}, inplace= True)
st.subheader('Mappa dei parcometri di Roma')
st.map(df_parcometri,zoom=11)


tariffa = df_parcometri['Tariffa'].apply(lambda x : x[0:7] if('ZONA' in x ) else x[0:15]).value_counts()
#tariffa
#tariffa.apply(lambda x : x.index()[:,6])
st.bar_chart(tariffa)
tar = df_parcometri['Tariffa'].drop_duplicates()
tar