import ee
import streamlit as st
import geemap.folium as geemap

def getNLCD(year):
    dataset = ee.ImageCollection("USGS/NLCD_RELEASES/2019_REL/NLCD")
    nlcd = dataset.filter(ee.Filter.eq("system:index", year)).first()
    landcover = nlcd.select("landcover")
    return landcover

st.header("National Land Cover Database (NLCD)")
row1_col1, row1_col2 = st.columns([3, 1])
Map = geemap.Map()
years = ["2001", "2004", "2006", "2008", "2011", "2013", "2016", "2019"]
with row1_col2:
    selected_year = st.multiselect("Select a year", years)
    add_legend = st.checkbox("Show legend")
if selected_year:
    for year in selected_year:
        Map.addLayer(getNLCD(year), {}, "NLCD " + year)
    if add_legend:
        Map.add_legend(title="NLCD Land Cover", builtin_legend="NLCD")
    with row1_col1:
        Map.to_streamlit(height=600)
else:
    with row1_col1:
        Map.to_streamlit(height=600)
