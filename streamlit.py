import streamlit as st
import streamlit.components.v1 as componants
from pivottablejs import pivot_ui
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_excel('company_dataset.xlsx')
print(df)
st.title('LeadGeneration')
t=pivot_ui(df)
with open(t.src) as t:
    

    componants.html(t.read(),width=900,height=1000,scrolling=True)



