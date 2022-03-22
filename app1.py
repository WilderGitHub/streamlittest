import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings("ignore")
x = st.slider('head',3,10)
#st.write(x, 'cuadradito', x * x)

#@st.cache
#def cargar():
#    tienda = pd.read_csv("store_data.csv")
#    return tienda
#vuelosTrain = st.cache(pd.read_csv)("vuelosTrain.csv")#, header=None)
vuelosTrain = pd.read_csv("vuelosTrain.csv")#, header=None)
#vuelosTrain = st.cache(vuelosTrain.drop(labels=["Unnamed: 0"],axis=1,inplace=True))
vuelosTrain.drop(labels=["Unnamed: 0"],axis=1,inplace=True)
#vuelosTrain.head()
st.dataframe(vuelosTrain.head(x))

with st.sidebar:
    option = st.selectbox(
     'Calificaciones de acuerdo a servicios ofrecidosHistogramas de:',
     ("Inflight wifi service", "Departure/Arrival time convenient", "Ease of Online booking", "Gate location", "Food and drink", "Online boarding", "Seat comfort", "Inflight entertainment", "On-board service", "Leg room service", "Baggage handling", "Checkin service", "Inflight service", "Cleanliness"))

#st.write('You selected:', option)
arr = vuelosTrain[option]
fig, ax = plt.subplots()
ax.hist(arr, bins=10)
st.pyplot(fig)

y = st.selectbox(
     'Histogramas de variables cuantitativas:',
     ("Age", "Flight Distance", "Departure Delay in Minutes", "Arrival Delay in Minutes"))

#st.write('You selected:', option)
arr = vuelosTrain[y]
fig, ax = plt.subplots()
ax.hist(arr, bins=50)
st.pyplot(fig)
