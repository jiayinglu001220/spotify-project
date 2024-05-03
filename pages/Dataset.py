#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st


# In[5]:


st.header("Data Source 1: Existing Source (Kaggle)")
st.write('''
          https://www.kaggle.com/datasets/rakkesharv/spotify-top-10000-streamed-songs 

          Description: This dataset from Kaggle contains top 10000 streamed songs in Spotify.
          It has 9 columns contains Spotify ranking, artist name, song name, number of days 
          since the release of the song, number of times inside top 10, peak position attained, 
          number of times Peak position attained, total number of streams during peak position, 
          and total stream.
          ''')

st.header("Data Source 2: API")
st.write('''
          https://developer.spotify.com/documentation/web-api  

          Description: This API is Spotify official API for developer. It provides access to 
          Spotify’s vast catalog of music. This API offers developers a wide range of functionalities, 
          enabling them to retrieve detailed information on artists, albums, and tracks, conduct searches, 
          and access user profiles.
          ''')

st.header("Data Source 3: Web-scraped Dataset")
st.write('''
        https://www.chosic.com/list-of-music-genres/  

        Description: This website has an extensive collection of over 6000 music genres, categorized under
        broad categories such as pop, hip hop, electronic, R&B, rock, and more. Each genre is meticulously 
        organized within these overarching categories.
        ''')

st.header("How the datasets related to each other?")
st.write('''
        These three datasets collectively offer a comprehensive view of the music landscape. The Kaggle dataset
        provides artist name and song name of top 10000 streamed songs in Spotify. By leveraging the Spotify API,
        we can enrich this dataset with additional information such as genre classifications and release date for
        corresponding songs. The music genre website provides a list of broad music category, and under each 
        category including a list of sub-genres (the genre name we retrieved using the Spotify API). Dataset 3 
        essentially provides dictionary style data, where the key is the high level genre(rock) and the value is
        a list of specific genres(revival clang rock, punk rock, etc). I will use the specific genre retrieved from
        Spotify api along with a dictionary to get the corresponding high level genre. Therefore, the 10000 popular
        songs in dataset 1 will only have around 15 genres instead of 6000+ genres, which will provide a more meaningful
        analysis.
        ''')


# In[ ]:




