import pandas as pd
import folium

ctx = '../data/'
csv = ctx+'CCTV_in_Seoul.csv'
xls = ctx+'population_in_Seoul.xls'
cctvdata = pd.read_csv(csv)
popdata = pd.read_excel(xls)
print(cctvdata.head(),popdata.head())
