import os
import sys
import json
import spotipy
import webbrowser
import csv
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
artists = ['Taylor Swift', 'Ariana Grande', 'Shawn Mendes', 'Maroon 5', 'Adele', 'Justin Bieber', 'Ed Sheeran', 'Justin Timberlake', 'Charlie Puth', 'John Mayer', 'Lorde', 'Fifth Harmony', 'Lana Del Rey', 'James Arthur', 'Zara Larsson', 'Pentatonix',
    'Kendrick Lamar', 'Post Malone', 'Drake', 'Kanye West', 'Eminem', 'Future', '50 Cent', 'Lil Wayne', 'Wiz Khalifa', 'Snoop Dogg', 'Macklemore', 'Jay-Z',
    'Bruno Mars', 'Beyonce', 'Enrique Iglesias', 'Stevie Wonder', 'John Legend', 'Alicia Keys', 'Usher', 'Rihanna',
    'Kygo', 'The Chainsmokers', 'Illenium', 'Marshmello', 'Calvin Harris', 'Martin Garrix', 'Slander',
    'Coldplay', 'Elton John', 'One Republic', 'Jason Mraz', 'Eden',
    'Frank Sinatra', 'Michael Buble', 'Norah Jones']
playlists = []
# Create our spotify object with permissions
sp = spotipy.Spotify(auth=token)

user = sp.current_user()
name = user['display_name'].split(' ')
followers = user['followers']['total']
print('Welcome %s to the Spotify API!' %(str(name[0])))
print('You have %d followers.' %(followers))

for i in range(1, len(artists)-47):
    searchq = "This Is " + artists[i]
    search = sp.search(searchq, type="playlist")
    if search['playlists']['items'][0]['name'] == searchq and search['playlists']['items'][0]['owner']['id'] == 'spotify':
        playlist_id = search['playlists']['items'][0]['id']
        playlists.append(playlist_id)

df = pandas.DataFrame(data=playlists)