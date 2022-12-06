#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import colorcet as cc
import holoviews as hv
import hvplot.pandas
from holoviews.element.tiles import EsriImagery
hvplot.extension('matplotlib','plotly')
hvplot.output(backend='bokeh')

df0 = pd.read_csv("firesCleaned_0.csv")
df1 = pd.read_csv("firesCleaned_1.csv")
df2 = pd.read_csv("firesCleaned_2.csv")
df3 = pd.read_csv("firesCleaned_3.csv")

# Creating smaller dataframes to analyze
df0Map = df0[['Latitude', 'Longitude']]
df1Map = df1[['Latitude', 'Longitude']]
df2Map = df2[['Latitude', 'Longitude']]
df3Map = df3[['Latitude', 'Longitude']]

dfMap1 = pd.concat([df0Map, df1Map])
del df0Map
del df1Map

dfMap2 = pd.concat([df2Map, df3Map])
del df2Map
del df3Map

df = pd.concat([dfMap1, dfMap2])
del dfMap1
del dfMap2

map_tiles = EsriImagery().opts(alpha=0.5, width=700, height=480, bgcolor='black')

plot = df.hvplot(
    'Longitude', 
    'Latitude', 
    kind='points',
    geo=True, 
    xlabel='Longitude',
    ylabel='Latitude',
    rasterize=True, 
    cmap=cc.fire, 
    cnorm='eq_hist',
    title='Interactive Map for Wildfire Data',  
    colorbar=True).opts(colorbar_position='bottom')
    
chart = map_tiles * plot

hvplot.show(chart)

