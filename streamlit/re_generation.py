import pandas as pd
import streamlit as st
import altair as alt
from pathlib import Path
from datetime import date
import os

today = date.today()
path = f"data/processed/tw/re_generation_m_{today.strftime('%Y-%m-%d')}.csv"

df = pd.read_csv(path, index_col=1)
df = df.drop(columns=['Unnamed: 0'])

all_types = df['Type'].unique()
selected_type = st.selectbox("Select Type", all_types)