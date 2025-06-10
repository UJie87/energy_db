import streamlit as st
import glob
import yaml
import pandas as pd
from pathlib import Path
import re


def load_frontmatter(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        # Parse YAML frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_part = parts[1]
            body_part = parts[2]
            meta = yaml.safe_load(yaml_part)
            return meta, body_part.strip()
    return {}, content.strip()



st.title("Mogoo- Asia Energy Database")
st.write("This is a demo for the Mogoo- Asia Energy Database!")

files =  glob.glob("policies/*.md")

posts = []
for f in files:
    meta, body = load_frontmatter(f)
    post_obj ={
        'metadata': meta,
        'body': body
    }
    posts.append(post_obj)

meta_df = pd.DataFrame([p['metadata'] | {"file":f} for p, f in zip(posts, files)])

meta_df['effective_year'] = meta_df['effective_year'].astype(str)

policy_label= meta_df['country'] + "-" + meta_df['topic'] + "-" + meta_df['effective_year'].astype(str)
policy = st.selectbox(
    "Choose a policy",
    policy_label
)
post= posts[policy_label.tolist().index(policy)]


with st.container(border=True):
    st.markdown(f"## {post['metadata']['country']} {post['metadata']['policy_id']}")
    col1,col2, col3, col4 = st.columns([1, 1, 1, 1])
    col1.metric("Country", post['metadata']['country'])
    col2.metric("Effective Year", post['metadata']['effective_year'])
    col3.metric("Status", post['metadata']['status'])
    col4.metric("Topic", post['metadata']['topic'])

# split the cotent into summary
RAW = post['body']
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
