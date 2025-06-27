import json, folium, streamlit as st
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Taiwan Offshore Wind Potential Site Map',
    layout = "wide"
)

with open('osw_bbox.geojson', encoding='utf-8') as f:
    gjs=json.load(f)

detailed_df = pd.read_csv("data/processed/tw/tw_osw_detailed.csv")

st.title('Taiwan Offshore Wind Potential Site Map')

m = folium.Map(location=[23.7, 120.5], zoom_start=7, tiles="CartoDB positron")

folium.GeoJson(
    gjs,
    name="bbox",
    tooltip=folium.GeoJsonTooltip(fields=["site_id"], aliases=[""]),
    style_function=lambda _: {"fillOpacity": 0.15, "weight": 1, "color": "#3186cc"},
    highlight_function=lambda _: {"weight": 3, "color": "#ff7800"},
).add_to(m)

map_data = st_folium(m, width=1100, height=700, key='TW_offshore_map')

clicked = map_data.get("last_object_clicked_tooltip")


if clicked:
    site_id = int(clicked)

    subset = detailed_df.loc[detailed_df['site_id']==site_id]

    st.write(f'Offshore wind site {site_id} has {(len(subset))} offshore wind farm(s)')

    st.dataframe(
        subset.rename(columns={
            'name_zh': '案場名稱',
            'name_en': 'Wind Farm',
            'status': 'Status',
            'capacity_mw': 'Capacity(MW)',
            'stakeholders': 'developers',
            'COD': 'COD',
            'offtaker': 'offtaker'
        }).drop(columns=['site_id', 'note']).set_index('phase', drop=True)
    )

else:
    st.info("click one site to see detailed OSW farm list")