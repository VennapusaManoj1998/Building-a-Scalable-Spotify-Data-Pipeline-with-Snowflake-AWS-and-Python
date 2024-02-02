#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install spotipy


# In[56]:


import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


# In[8]:


client_credentials_manager = SpotifyClientCredentials(client_id="dfdba6e22a27416192754d0e561285bb", client_secret="cb45bb7fdffe4d50ba17b2d4ebd8a24f")


# In[11]:


sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[17]:


playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DWTt3gMo0DLxA"


# In[20]:


spy_URL = playlist_link.split("/")[-1].split('?')[0]


# In[23]:


data = sp.playlist_tracks(spy_URL)


# In[ ]:


len(data['items'])


# In[33]:


data['items'][0]['track']['album']['id']


# In[32]:


data['items'][0]['track']['album']['name']


# In[34]:


data['items'][0]['track']['album']['release_date']


# In[38]:


data['items'][0]['track']['album']['external_urls']['spotify']


# In[43]:


album_list = []
for row in data['items']:
    album_id = row['track']['album']['id']
    album_name = row['track']['album']['name']
    album_release_date = row['track']['album']['release_date']
    album_total_tracks = row['track']['album']['total_tracks']
    album_url = row['track']['album']['external_urls']['spotify']
    album_element = {'album_id':album_id, 'album_name':album_name, 'album_release_date':album_release_date, 
                     'album_total_tracks':album_total_tracks, 'album_url':album_url }
    album_list.append(album_element)
    


# In[44]:


album_list


# In[49]:


data['items'][0]['track']['artists']


# In[54]:


artist_list = []
for row in data['items']:
    for key, value in row.items():
        if key == "track":
            for artist in value["artists"]:
                artist_dict = {"artist_id":artist["id"], "artist_name":artist["name"],"external_url":artist["href"]}
                artist_list.append(artist_dict)
    


# In[55]:


artist_list


# In[57]:


song_list = []
for row in data['items']:
    song_id = row['track']['id']
    song_name = row['track']['name']
    song_url = row['track']['external_urls']['spotify']
    song_element = {'song_id':song_id, 'song_name':song_name, 'song_url':song_url }
    song_list.append(song_element)
    


# In[58]:


album_df = pd.DataFrame(album_list)


# In[60]:


album_df


# In[61]:


album_df = album_df.drop_duplicates(subset="album_id")


# In[62]:


album_df


# In[64]:


artist_df = pd.DataFrame(artist_list)


# In[67]:


artist_df = artist_df.drop_duplicates(subset="artist_id")
artist_df


# In[70]:


song_df = pd.DataFrame(song_list)


# In[72]:


song_df = song_df.drop_duplicates(subset="song_id")
song_df


# In[ ]:




