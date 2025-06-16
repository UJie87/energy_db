import streamlit as st
import glob
import yaml
import pandas as pd
from pathlib import Path
import re


st.set_page_config(
    page_title = 'Mogoo DB'
)

st.title("Mogoo- Asia Energy Database")
st.write("This is a demo for the Mogoo- Asia Energy Database!")

st.subheader("APAC Renewable Energy Procurement Mechanism Overview")
data = [
    {"Country": "Indonesia", "Electricity Market Structure": "competitive wholesale & retail", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟩", "Utility Green Tariff": ""},
    {"Country": "Japan", "Electricity Market Structure": "competitive wholesale & retail", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟩", "Utility Green Tariff": ""},
    {"Country": "Malaysia", "Electricity Market Structure": "regulated", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟨", "Utility Green Tariff": "🟩"},
    {"Country": "Philippine", "Electricity Market Structure": "hybrid (wholesale without retail)", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟥", "Utility Green Tariff": ""},
    {"Country": "Singapore", "Electricity Market Structure": "competitive wholesale & retail", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟩", "Utility Green Tariff": ""},
    {"Country": "South Korea", "Electricity Market Structure": "hybrid (wholesale without retail)", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟩", "Utility Green Tariff": ""},
    {"Country": "Taiwan", "Electricity Market Structure": "regulated", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟩", "Virtual Off-site CPPA": "🟥", "Utility Green Tariff": "🟨"},
    {"Country": "Thailand", "Electricity Market Structure": "regulated", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟨", "Virtual Off-site CPPA": "🟥", "Utility Green Tariff": "🟩"},
    {"Country": "Viet Nam", "Electricity Market Structure": "regulated", "On-site CPPA": "🟩", "Physical Off-site CPPA": "🟨", "Virtual Off-site CPPA": "🟥", "Utility Green Tariff": "🟩"}
]

df=pd.DataFrame(data)

edited = st.data_editor(
    df,
    column_config={
        "On-site CPPA": st.column_config.TextColumn(disabled=True),
        "Remark": st.column_config.TextColumn(disabled=True),
    },
    use_container_width=True,
    hide_index= True,
    disabled=True,
    num_rows="fixed",
    key="mechanism_table"
)

st.subheader("Each Country Mechanism Details")
select_country = st.selectbox("Select a country", df['Country'].unique())




