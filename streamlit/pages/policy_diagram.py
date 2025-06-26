from streamlit_agraph import agraph, Node, Edge, Config
import streamlit as st

st.set_page_config(
    page_title = 'Policy Relationship Diagram',
    layout = "wide"
)

st.title("Mogoo- Policy Relationship Diagram")

nodes = [
    Node(id="TW_ELE_2024", label="電業法", size= 30, color='gray'),
    Node(id="TW_OSW_2024", label="離岸風子法", size=20, color='green'),
    Node(id="TW_FiT_2024", label="躉購費率", size=20, color='blue'),
    Node(id="TW_OSW_imple_2024", label="作業要點", size=10, color='orange')
]

edges = [
    Edge(source="TW_ELE_2024", target="TW_OSW_2024", label="子法"),
    Edge(source="TW_ELE_2024", target="TW_FiT_2024", label="子法"),
    Edge(source="TW_OSW_2024", target="TW_OSW_imple_2024", label="作業要點")
]

config = Config(
    width=2000,
    height=1000,
    direction=True,
    nodeHighlightBehavior=True,
    highlightColor='#F7A7A6',
    collapsible=True
)

agraph(nodes=nodes, edges=edges, config=config)
