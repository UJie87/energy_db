import json, folium, streamlit as st
from streamlit_folium import st_folium
import streamlit as st

with open('osw_bbox.geojson', encoding='utf-8') as f:
    gjs=json.load(f)

st.title('Taiwan Offshore Wind Potential Site Map')

m = folium.Map(location=[23.7, 120.5], zoom_start=7, tiles="CartoDB positron")

folium.GeoJson(
    gjs,
    name="bbox",
    tooltip=folium.GeoJsonTooltip(fields=["site_id"], aliases=["site："]),
    style_function=lambda _: {"fillOpacity": 0.15, "weight": 1, "color": "#3186cc"},
    highlight_function=lambda _: {"weight": 3, "color": "#ff7800"},
).add_to(m)

st_folium(m, width=1100, height=700)