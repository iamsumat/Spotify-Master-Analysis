# import os,sys,json,spotipy,webbrowser,pyperclip
# import spotipy.util as util
# from json.decoder import JSONDecodeError
# from spotipy.oauth2 import SpotifyClientCredentials


# client_id = 'f9661a146caa40909c47e655d4f584b8'
# client_secret = '4632899dfdc24090ae2e44aad97b359b'

# client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# name = 'Taylor Swift'
# result = sp.search(name)
# print(json.dumps(result['tracks']['items'], indent=5))
# sp._get("https://api.spotify.com/v1/playlists/21THa8j9TaSGuXYNBU5tsC/tracks")

import os
import sys
import json
import spotipy
import pandas
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
# username = sys.argv[1]
username = 'simar2222'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope, client_id='f9661a146caa40909c47e655d4f584b8',client_secret='4632899dfdc24090ae2e44aad97b359b',redirect_uri='https://www.google.com/') # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Artists for the analysis
artists = ['Taylor Swift', 'Ariana Grande', 'Shawn Mendes', 'Maroon 5', 'Adele', 'Justin Bieber', 'Ed Sheeran', 'Justin Timberlake', 'Charlie Puth', 'John Mayer', 'Lorde', 'Fifth Harmony', 'Lana Del Rey', 'James Arthur',
    'Kendrick Lamar', 'Post Malone', 'Drake', 'Kanye West', 'Eminem', 'Future', 'Snoop Dogg', 'Macklemore', 'Jay-Z',
    'Bruno Mars', 'Beyoncé', 'Drake', 'Stevie Wonder', 'John Legend', 'Alicia Keys', 'Rihanna', 'Michael Jackson',
    'Kygo', 'The Chainsmokers', 'Illenium', 'Marshmello', 'Calvin Harris', 'Martin Garrix', 'Eden', 'Prince',
    'Coldplay', 'Elton John', 'OneRepublic', 'Jason Mraz', 'Metallica', 'The Beatles', 'Guns N\' Roses',
    'Frank Sinatra', 'Michael Bublé', 'Norah Jones', 'David Bowie']
playlists = []
n = 0

# Create our spotify object with permissions
sp = spotipy.Spotify(auth=token)

user = sp.current_user()
name = user['display_name'].split(' ')
followers = user['followers']['total']
print('Welcome %s to the Spotify API!' %(str(name[0])))
print('You have %d followers.' %(followers))

print('Searching for playlists...')
for i in range(len(artists)):    
    searchq = "This Is " + artists[i]
    search = sp.search(searchq, type="playlist")
    if str.lower(search['playlists']['items'][0]['name']) == str.lower(searchq) and search['playlists']['items'][0]['owner']['id'] == 'spotify':
        playlist_id = search['playlists']['items'][0]['id']
        playlists.append(playlist_id)
        print("Found for " + str(artists[i]))
        # n += 1
    else:
        print("Playlist not found for " + (str(artists[i])), end='\n')

# print("Total - " + str(n))

print("Printing to CSV...")
df = pandas.DataFrame(data=playlists)
df.to_csv('playlisturi.csv', sep=',', index=False, header=False)
print("Finished")





    # with open('{}-content.json'.format(artists[i]), 'w') as outfile:
    #     json.dump(search, outfile)
# print(json.dumps(search['playlists']['items'], skipkeys=True, indent=4))

    

# tracks_url = search['playlists']['items']['tracks'][0]['href']
# if search['playlists']['items'][0]['name'] = str.lower(searchq):
# def get_playlist_content(playlist_id,sp):
#     offset = 0
#     songs = []
#     while True:
#         content = sp.user_playlist_tracks('spotify', playlist_id, fields = None, limit=100, offset=offset, market=None)
#         songs += content['items']
#         if content['next'] is not None:
#             offset += 100
#         else:
#             break
#     with open('{}-{}-content.json'.format(username, playlist_id), 'w') as outfile:
#         json.dump(songs,outfile)
        
# def get_user_playlist(username, sp):
#     playlists = sp.user_playlists('spotify', limit=200)
#     for playlist in playlists['items']:
#         print("Name: {}, Number of songs: {}, Playlist ID: {} ".
#               format(playlist['name'], playlist['tracks']['total'],playlist['id']))

# get_user_playlist('simar2222', sp)
# # get_playlist_content('37i9dQZF1DX2rBR3X9E86S',sp)







######################################################################
# Loop through all artist names in the list - 50
# Get the This Is playlist of the artist
# Get the playlist id
# Store all ids in a .csv file


#https://spotipy.readthedocs.io/en/2.6.3/ -  audio_analysis, audio_features
# user_playlist_tracks