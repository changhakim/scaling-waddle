import pandas as pd
import folium

ctx = '../data/'
csv = ctx+'CCTV_in_Seoul.csv'
xls = ctx+'population_in_Seoul.xls'
cctv_data = pd.read_csv(csv)
pop_data = pd.read_excel(xls)

cctv_data_schema = cctv_data.columns
pop_data_schema = pop_data.columns
print(pop_data_schema)
"""
cctv_data 스키마
Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
pop_data 스키마
Index(['기간', '자치구', '세대', '인구', '인구.1', '인구.2', '인구.3', '인구.4', '인구.5', '인구.6',
       '인구.7', '인구.8', '세대당인구', '65세이상고령자'],
      dtype='object')
"""
