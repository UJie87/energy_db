import pandas as pd
import numpy as np
import requests
import json
import re
import datetime
import pathlib

URL = "https://www.esist.org.tw/api/v1/zone/monthly/4/1"
HEADERS = {"accept": "application/json",
           "accept-encoding": "gzip, deflate"}

r = requests.get(URL,headers = HEADERS, timeout=30)

data = r.json()

df_raw = pd.DataFrame(data['再生能源'])

header_map ={
    'Column2': ('Total', '', 'MWh'),
    'Column3': ('Hydro', '', 'MWh'),
    'Column5': ('Geothermal', '', 'MWh'),
    'Column7': ('Solar', '', 'MWh'),
    'Column9': ('Wind', 'Subtotal', 'MWh'),
    'Column11': ('Wind', 'Onshore', 'MWh'),
    'Column13': ('Wind', 'Offshore', 'MWh'),
    'Column15': ('Biomass', 'Subtotal', 'MWh'),
    'Column17': ('Biomass', 'Solid', 'MWh'),
    'Column19': ('Biomass', 'Biogas', 'MWh'),
    'Column21': ('Waste', '', 'MWh')
}

mwh_cols = list(header_map.keys())
header_tuples = list(header_map.values())
custom_header = pd.MultiIndex.from_tuples(header_tuples, names=['Type', 'SubType', 'Unit'])

data_rows = df_raw.iloc[5:].dropna(subset=['Column23']).copy()

df_final = pd.DataFrame()
for col in mwh_cols:
    if col in data_rows:
        df_final[col] = data_rows[col]
    else:
        df_final[col] = np.nan

df_final.columns = custom_header
df_final.index = data_rows['Column23']
df_final.index.name = 'Period'

df_stacked = df_final.stack(level=['Type', 'SubType', 'Unit']).reset_index()
df_stacked.rename(columns = {0: 'Generation'}, inplace=True)
df_stacked.drop(columns=['Unit'], inplace=True)
df_stacked['SubType'] = np.where(df_stacked['SubType'] == '', 'Subtotal', df_stacked['SubType'])

date_pattern = r'(^\d{4}$)|(^\d{4}\/\d{2}$)'
is_date_format = df_stacked['Period'].str.match(date_pattern)
df_clean = df_stacked[is_date_format]
print(df_clean.tail())


today = datetime.date.today().isoformat()

output_csv_path = f'data/processed/tw/re_generation_m_{today}.csv'
df_clean.to_csv(output_csv_path, index=True)
print(f"Data saved to {output_csv_path}")


'''
raw_data_path = pathlib.Path(f'data/raw/re_generation_m_{today}.json')
with raw_data_path.open('w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
'''