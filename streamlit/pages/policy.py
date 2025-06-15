import streamlit as st
import frontmatter
import glob
import os
import pandas as pd
from pathlib import Path
import re

files =  glob.glob("C:/Users/You Jie Tsai/OneDrive/energy_db/policies/*.md")
posts = [frontmatter.load(f) for f in files]

meta_df = pd.DataFrame([p.metadata | {"file":f} for p, f in zip(posts, files)])

policy_label= meta_df['country'] + "-" + meta_df['topic'] + "-" + meta_df['effective_year'].astype(str)
policy = st.selectbox(
    "Choose a policy",
    policy_label
)
post= posts[policy_label.tolist().index(policy)]


with st.container(border=True):
    st.markdown(f"## {post.metadata['country'] + " " + post.metadata['policy_id']}")
    col1,col2, col3, col4 = st.columns([1, 1, 1, 1])
    col1.metric("Country", post.metadata['country'])
    col2.metric("Effective Year", post.metadata['effective_year'])
    col3.metric("Status", post.metadata['status'])
    col4.metric("Topic", post.metadata['topic'])

# split the cotent into summary
RAW = post.content
if "<!--SUMMARY SPLIT-->" in RAW:
    summary, full = RAW.split("<!--SUMMARY SPLIT-->", 1)
else:
    summary, full = RAW, ""

st.markdown(summary, unsafe_allow_html=True)

parts = re.split(r"<!--CARD:(.*?)-->", full)

cards = [(parts[i+1].strip(), parts[i+2].strip())
         for i in range(0, len(parts)-1, 2)]

for title, content in cards:
    with st.expander(title, expanded=False):
        st.markdown(content, unsafe_allow_html=True)