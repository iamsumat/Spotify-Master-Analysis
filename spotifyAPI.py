import os, time
import sys
import json
import spotipy
import pandas
import spotipy.util as util
from json.decoder import JSONDecodeError

t0 = time.time()

# Get the username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope, client_id='f9661a146caa40909c47e655d4f584b8',client_secret='4632899dfdc24090ae2e44aad97b359b',redirect_uri='https://www.google.com/') # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Artists for the analysis
artists = ['Taylor Swift', 'Ariana Grande', 'Shawn Mendes', 'Maroon 5', 'Adele', 'Twenty One Pilots', 'Ed Sheeran', 'Justin Timberlake', 'Charlie Puth', 'John Mayer', 'Lorde', 'Fifth Harmony', 'Lana Del Rey', 'James Arthur',
    'Kendrick Lamar', 'Post Malone', 'Drake', 'Kanye West', 'Eminem', 'Future', 'Snoop Dogg', 'Macklemore', 'Jay-Z',
    'Bruno Mars', 'Beyoncé', 'Drake', 'Stevie Wonder', 'John Legend', 'The Weeknd', 'Rihanna', 'Michael Jackson',
    'Kygo', 'The Chainsmokers', 'Illenium', 'Marshmello', 'Avicii', 'Martin Garrix', 'Eden', 'Prince',
    'Coldplay', 'Elton John', 'OneRepublic', 'Jason Mraz', 'Metallica', 'The Beatles', 'Guns N\' Roses',
    'Frank Sinatra', 'Michael Bublé', 'Norah Jones', 'David Bowie']

# Initialize empty dataframe with columns
allfeatures = pandas.DataFrame(columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'duration_ms', 'time_signature'])

# Create our spotify object with permissions
sp = spotipy.Spotify(auth=token)

# Print user info
user = sp.current_user()
name = user['display_name'].split(' ')
followers = user['followers']['total']
print('Welcome %s to the Spotify API!' %(str(name[0])))
print('You have %d followers.' %(followers))

print('Searching for playlists...')


for i in range(len(artists)):    
    playlists,track_uri = [],[]
    searchq = "This Is " + artists[i]
    search = sp.search(searchq, type="playlist")
    if str.lower(search['playlists']['items'][0]['name']) == str.lower(searchq) and search['playlists']['items'][0]['owner']['id'] == 'spotify':
        playlist_id = search['playlists']['items'][0]['id']
        playlists.append(playlist_id)
        print("Found for " + str(artists[i]))
        # n += 1
    else:
        print("Playlist not found for " + (str(artists[i])), end='\n')

    playlist_content = sp.user_playlist_tracks('spotify', playlist_id=playlist_id)
    for n in range(100):
        try:
            track = playlist_content['items'][n]['track']['uri']
        except:
            print("Total # of tracks are " + str(n-1))
            break
        track_uri.append(track)
    audio_feat = sp.audio_features(tracks=track_uri)
    aud = pandas.DataFrame(data=audio_feat)
    aud_mean = aud.mean()
    allfeatures = pandas.DataFrame.append(allfeatures, aud_mean, ignore_index=True)
    print("#%d. Audio features for %s extracted." %(i+1,artists[i]))

allfeatures = allfeatures.set_index([pandas.Index(artists)])
# print(allfeatures.head())

allfeatures.to_csv('audio_features.csv',sep=',')
print("\n\nData saved to audio_features.csv\n")

t1 = time.time()
print("Total time for the operation: %fsec\n" %(t1-t0))