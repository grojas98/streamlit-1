# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:45:57 2022

@author: groja
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import pandas as pd
from itertools import count
import seaborn as sns
import time
import psycopg2 as pg

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Mapa de calor Sabanilla')

st.markdown("""
Figura con mapa de calor actualizado en tiempo real
con números **aleatorios**.
""")

hm_df = pd.DataFrame()

state = 0

fig, ax = plt.subplots()

heat_map = st.empty()
series_graph = st.empty()

start = st.button('Start simulation')

if start:
    state = 1

stop = st.button('Stop')

if state == 1:
    while True:
        plt.close(fig)
        fig, ax = plt.subplots()
        sens = [random.randrange(0,4000,1) for i in range(24)]
        df_data = {
            'col1': [sens[0],sens[1],sens[2]],
            'col2': [sens[3],sens[4],sens[5]],
            'col3': [sens[6],sens[7],sens[8]],
            'col4': [sens[9],sens[10],sens[11]],
            'col5': [sens[12],sens[13],sens[14]],
            'col6': [sens[15],sens[16],sens[17]],
            'col7': [sens[18],sens[19],sens[20]],
            'col8': [sens[21],sens[22],sens[23]]
        }
        
        hm_df = pd.DataFrame.from_dict(df_data)
        sns.heatmap(hm_df,vmin=0,vmax=4068,annot=True,fmt='.0f',ax=ax)
        heat_map.write(fig)
        time.sleep(0.5)
        if stop:
            state = 0
            break

    