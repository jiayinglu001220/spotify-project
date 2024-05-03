#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[15]:

!pip install plotly

import streamlit as st
import pandas as pd
import plotly.express as px


# ## Data Cleaning

# In[16]:


df = pd.read_csv('top_songs.csv')
# Release year for each song is extracted as an integer for further analysis.
df['Year'] = pd.to_datetime(df['Release Date'], errors='coerce', exact=False)
df.dropna(subset=['Year'], inplace=True)
df['Year'] = df['Year'].dt.year.astype(int)


# ## Data Visualization

# In[17]:


# Calculate total streams per year for each genre.
genre_yearly_streams = df.groupby(['Year', 'Broad Genre'])['Total Streams'].sum().reset_index()


# In[18]:


# Add interation with the plot
selected_genres = st.sidebar.multiselect('Select genres to display:', options=df['Broad Genre'].unique(), default=[])

# Plotting
st.title('Evolution of Music Genre Popularity on Spotify')
st.write('Created by Jiaying Lu')


filtered_data = genre_yearly_streams[genre_yearly_streams['Broad Genre'].isin(selected_genres)]
if selected_genres:
    filtered_data = genre_yearly_streams[genre_yearly_streams['Broad Genre'].isin(selected_genres)]
else:
    filtered_data = genre_yearly_streams

# Use Log scale to fully display all the datapoints clearly.
plot = px.line(filtered_data, x="Year", y="Total Streams", color="Broad Genre",
              labels={"Total Streams": "Total Streams (log scale)"},
              title="Total Streams by Genre Over Time",
              log_y=True)  
# Adjust Interation feature of the plot
plot.update_layout(xaxis=dict(tickmode='linear', dtick=10))

st.plotly_chart(plot)

st.header('How to Use This Webapp')
st.write('''
         1. Use the sidebar to select different genres to display on the plots.
         2. Hover over the plots to see detailed data points.
         3. Click button to listen to sample music for specific genre.
         ''')

st.header('How to Understand this plot')
st.write('''
          Each line in the plot represents the popularity trend of a specific genre over time, 
          measured in total streams. A logarithmic scale is used to ensure all data points are 
          visible and clear, even when there are large disparities in stream counts.
          ''')

st.header('Conclusions')
st.write('''
          The analysis of Spotify streaming data over the past decades reveals distinct trends
          in music genre popularity. Specifically, genres such as Pop and Hip-Hop have not only
          seen a significant rise in popularity but have also consistently dominated the market. 
          This trend underscores their widespread appeal and dynamic adaptability to changing
          music consumption patterns. Conversely, other genres like Rock, R&B, and Country have
          experienced more stable patterns, with neither dramatic increases nor significant declines.
         ''')

st.header('Improvement')
st.write('''
          The interface could be improved, particularly the plot displaying total streams by genre
          over time. Currently, it might appear cluttered due to the overlapping of 15 genres. While
          a dropdown menu serves as a filter, exploring more effective ways to display the plot could
          enhance clarity and user experience.
         ''')


# In[ ]:




