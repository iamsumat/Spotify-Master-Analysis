# SPOTIFY MASTER ANALYSIS
An in-depth EDA of the top 50 artists of Spotify.

### Introduction
Each artist is unique in his style. Let it be *Eminem* who can dazzle everyone with his words or *Marshmello*, who you can bang your head to. Whether, you're a fan of *The Beatles* or you've been following *Coldplay* since they released their single 'Yellow', you'll know how music from each artist/band differs in so many ways.

Spotify is the most used audio streaming platform in the world. Today, it provides it's listeners with all kinds of music, podcasts and even videos from artists they love. Launched in 2008, it now provides access to over 50 million tracks worldwide. I'm sure you must be familiar with it by now and how it has made music easily accessible to all parts of the world.
Spotify recently launched a variety of playlists curated specifically for each user. These include:
1. Release Radar: a personalized playlist that allows users to stay up-to-date on new music released by artists they listen to the most.
2. Discover Weekly: a weekly generated playlist (updated on Mondays) that brings users two hours of custom-made music recommendations, mixing a user’s personal taste with songs enjoyed by similar listeners.
3. Daily Mix: a series of playlists that have “near endless playback” and mixes the user’s favorite tracks with new, recommended songs.

With these, I also recently discovered that Spotify has a 'This Is' playlist for every artist on the platform comprising of their most heard or most popular hits. One of Spotify’s best original features, “This Is” delivers on a major promise of the streaming revolution — the canonization and preservation of great artists’ repertoires for future generations to discover and appreciate. Spotify has provided us a shortcut, giving us curated lists for every artist and making it easier to discover new artists with their topmost tracks.

So, you've been listening to music all your life, you've grown up with some of your favourite artists. Have you ever wondered what makes these artists so likeable? Why is *Bruno Mars* and his music so widely liked around the world? Why music from bands like *Metallica* and *Guns N' Roses* pump you up? Or tunes from which artists get you up on your feet everytime?
Don't worry, I've got you covered.

### The Approach
The purpose of this project is to analyze the music that different artists on Spotify produce. For this analysis, I have made a list of top 50 artists from a wide range of genres.
For the study, I will access the [Spotify Web API](https://developer.spotify.com/documentation/web-api/), which provides data from the Spotify music catalog. This can be accessed via standard HTTPS requests to an API endpoint.
The Spotify API among other things, provide audio statistics and features such as danceability, valence and tempo for each track. Each feature measures an aspect of a song. Detailed information on how this data is extracted can be found in the docs [here](https://developer.spotify.com/documentation/web-api/reference/).

With the help of [Spotipy](https://github.com/plamere/spotipy) for Python, I induvidually searched for each artist in my list, extracted the unique URI of the "This Is" playlist. With each ID, I obtained a list of all the tracks in the playlist and extracted the audio features for each track using the Spotify API methods. Now, after extracting the features for each track, I calculated their mean to get a summary for each artist. This mean summary of all features was saved to a [csv](https://github.com/Sumat2222/Spotify-Master-Analysis/blob/master/audio_features.csv). This was then used to do an Exploratory Data Analysis with Pandas, Matplotlib and Seaborn in a Jupyter Notebook.

### Setup
Python needs to be installed for this to work. It can be downloaded in the below mentioned website - 
https://www.python.org/downloads/
After installing Python, you will need [Spotipy](https://github.com/plamere/spotipy) to work with the Spotify API.
Spotipy is a light weight Python library for the Spotify Web API. For full documentation, refer to [Spotify Online Documentation](http://spotipy.readthedocs.org/).

### Installation
With Python installed, just open the terminal and type this:
```python
    pip install spotipy
```
After installing Spotipy, you will need to create an app on https://developers.spotify.com/. On successfull creation, you will find an alphanumeric *client_id* and *client_secret* at the [Spotify Dashboard](https://developer.spotify.com/dashboard/).

### Usage
Specify your Spotify username as an argument when you run the program. It will then ask you to input your personal *client_id* and *client_secret*. Once you are done with that, Spotify will begin to authenticate your account with it's API.
For that, it will open a browser and redirect a link to www.google.com. When it does, copy the URL from the Address Bar and paste it in the terminal. This will successfully authenticate your app with the Spotify API.

Now, you can edit the artists list in the program with artists of your choice. Please keep in mind, to check Spotify for the correct spellings or if your artist's name contains special characters. For ex. *Beyoncé* or *Alizée*.

Now, sit back and relax and watch the magic happen!
The program will extract audio features of all songs in the artists' 'This Is' playlist, calculate their *mean* and save them under each of their names. These features are initally saved to a Pandas DataFrame and then exported to [audio_features.csv](https://github.com/Sumat2222/Spotify-Master-Analysis/blob/master/audio_features.csv).

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Further Goals
* Find out the relation between attributes using the correlation matrix.
* Extract track popularity data and use it for analysis.
* Apply K-Means Clustering to bind artists into groups based on their genre and plot scatterplots and radar charts to better visualise the extent of each feature across genre.