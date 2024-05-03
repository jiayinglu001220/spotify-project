#!/usr/bin/env python
# coding: utf-8

# In[36]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[37]:


# Data Cleaning
df = pd.read_csv('top_songs.csv')
df['Year'] = pd.to_datetime(df['Release Date'], errors='coerce', exact=False)
df.dropna(subset=['Year'], inplace=True)
df['Year'] = df['Year'].dt.year.astype(int)
df_grouped = df.groupby(['Year', 'Broad Genre'])['Total Streams'].sum().reset_index()
total_streams_per_year = df_grouped.groupby('Year')['Total Streams'].sum().reset_index()
total_streams_per_year.rename(columns={'Total Streams': 'Total Streams All Genres'}, inplace=True)
df_merged = pd.merge(df_grouped, total_streams_per_year, on='Year')
df_merged['Market Share'] = (df_merged['Total Streams'] / df_merged['Total Streams All Genres']) * 100


# In[38]:


# Data preprocessing for hip hop
hip_hop_data = df_merged[df_merged['Broad Genre'] == 'Hip Hop']
plot = px.area(hip_hop_data, x='Year', y='Market Share',
              title='Market Share of Hip-Hop Over Time',
              labels={'Market Share': 'Market Share of Hip-Hop (%)'})

st.header('Explore Top Music Genres')
st.subheader('Hip Hop')
st.plotly_chart(plot)

st.audio('audios/Drake_Behind_Barz.mp3', format='audio/mp3', start_time= 36, end_time = 60)

# Analysis of the plot
st.write('''
            Hip hop has consistently maintained a high market share compared to other leading music genres.
            The data indicates that it became mainstream in the 1990s, driven by the emergence of influential
            rappers and landmark albums that often addressed social issues.
         ''')


# In[39]:


# Data preprocessing for pop
pop_data = df_merged[df_merged['Broad Genre'] == 'Pop']
plot = px.area(pop_data, x='Year', y='Market Share',
              title='Market Share of Pop Over Time',
              labels={'Market Share': 'Market Share of Pop (%)'})


st.subheader('Pop')
st.plotly_chart(plot)

st.audio('audios/Ariana_Grande_3435.mp3', format='audio/mp3')

# Analysis of the plot
st.write('''
            Pop music holds the second highest market share over time. According to the plot, it gained
            popularity beginning in the 1880s and maintained a consistently high market share across
            subsequent decades. However, its market share has begun to decline in the recent decade due to
            the increasing diversity of music genres. 
         ''')


# In[40]:


# Data preprocessing for R&B
rb_data = df_merged[df_merged['Broad Genre'] == 'R&B']
plot = px.area(rb_data, x='Year', y='Market Share',
              title='Market Share of R&B Over Time',
              labels={'Market Share': 'Market Share of R&B (%)'})

st.subheader('R&B')
st.plotly_chart(plot)

st.audio('audios/SZA_Kiss_Me_More.mp3', format='audio/mp3', start_time= 10, end_time = 33)

# Analysis of the plot
st.write('''
            R&B gained popularity earlier than many other genres, achieving its highest market share in the
            1960s and 1970s. This surge in popularity may be attributed to the demographic shifts caused by
            the Great Migration, leading to a larger Black American audience. R&B briefly dominated the market
            in the 1980s but has since become less competitive in the music industry.
         ''')


# In[35]:


# Data preprocessing for Electronic
electronic_data = df_merged[df_merged['Broad Genre'] == 'Electronic']
plot = px.area(electronic_data, x='Year', y='Market Share',
              title='Market Share of Electronic Over Time',
              labels={'Market Share': 'Market Share of Electronic (%)'})


st.subheader('Electronic')
st.plotly_chart(plot)

st.audio('audios/Marshmello_Sell_Out.mp3', format='audio/mp3')

# Analysis of the plot
st.write('''
            Electronic music evolved in the late 1980s and 1990s, gaining popularity in the 2000s. While it
            hasn't reached the same level of popularity as hip hop and pop in recent years, it still maintains
            a significant market presence, bolstered by the rise of electronic music festivals. It is becoming
            increasingly popular among younger audiences.
         ''')


# In[ ]:




