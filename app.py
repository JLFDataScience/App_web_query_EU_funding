#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import urllib.request
import numpy as np
import requests
import pandas as pd
import json
#import io
import warnings
import time
import streamlit as st
#import plotly.express as px


@st.cache(ttl=60*60*24*7 ,max_entries=30)
def load_data():
    url = 'https://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json'
    response = requests.get(url)
    response_dict = json.loads(response.text)

    df=pd.DataFrame()
    for i in range(len(response_dict["fundingData"]["GrantTenderObj"])):
        df=df.append(pd.DataFrame([response_dict["fundingData"]["GrantTenderObj"][i]]))
    df_select = df[['title', 'callTitle', 'status', 'tags', 'url', 'procedureType']].reset_index(drop=True)
    df_select['status'] = df_select['status'].apply(lambda x: x.get('description'))
    df_select = df_select[df_select['status'] =='Open'].reset_index(drop=True)
    return df_select

df_select = load_data()

st.markdown('<style>description:{color: blue;}</style>', unsafe_allow_html=True)
#st.image('image/FGCSIC_logo.png', width=150)
st.image('image/logo_dataScience_V0.png', width=200)
st.title('🔎Consulta programas de financiación💷 de la UE')
st.markdown('<description>Desde este microsite, se puede consultar mediante palabras clave tanto en los tags '+
            'como en el título de los programas de financiación de la UE</description>', unsafe_allow_html=True)
st.sidebar.title('Buscar por palabras clave')
st.sidebar.markdown('seleccionando para buscar en el título o en los tags del programa')
####Prueba de campo de entrada vacío 
#vacio = st.empty()

#keyword = st.sidebar.text_input.
#click_clear = st.button('clear text input', key=1)
#if click_clear:
#    input = placeholder.text_input('text', value='', key=1)

keyword = st.sidebar.text_input("Intro keyword", value='')

#####Desde aquí funciona
#keyword = st.sidebar.text_input("Intro keyword", value='innovation')
select = st.sidebar.radio("Seleccionar campo de búsqueda:", ('Tags', 'Title'))

#Mostrar tabla búsqueda en tags
if (select == 'Tags') & (keyword != ''):
    pd.set_option ("max_colwidth", None)
    funding_kw = df_select[df_select.tags.str.join('-').str.contains(keyword, case=False) == True]['title']
    st.write(funding_kw)
    #st.dataframe(df_select[df_select.tags.str.join('-').str.contains(keyword, case=False) == True][['title','url']])
    st.table(df_select[df_select.tags.str.join('-').str.contains(keyword, case=False) == True][['title','url']])
elif (select == 'Title') & (keyword != ''):
    finding_title = df_select[df_select.title.str.contains(keyword, case=False) == True]['title']
    st.write(finding_title)
    #st.dataframe(df_select[df_select.title.str.contains(keyword, case=False) == True][['title','url']])
    st.table(df_select[df_select.title.str.contains(keyword, case=False) == True][['title','url']])
elif keyword == '':
    st.markdown('**Introduzca una palabra clave en el campo de búsqueda lateral para obtener resultados**')
    st.markdown('Puede usar el símbolo ***** para truncar las palabras de búsqueda')
    st.markdown('Puede usar el símbolo **|** para buscar varias palabras, similar al uso de "OR"')

