import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings("ignore")
x = st.slider('head',3,10)
st.write(x, 'cuadradito', x * x)

#@st.cache
#def cargar():
#    tienda = pd.read_csv("store_data.csv")
#    return tienda
vuelosTrain = st.cache(pd.read_csv)("vuelosTrain.csv", header=None)
vuelosTrain.drop(labels=["Unnamed: 0"],axis=1,inplace=True)
#vuelosTest.drop(labels=["Unnamed: 0"],axis=1,inplace=True)
vuelosTrain.head()
st.dataframe(vuelosTrain.head(x))