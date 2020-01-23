# SPOTIFY MASTER ANALYSIS

An in-depth EDA of the top 50 artists of Spotify.

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
Find out the relation between attributes using the correlation matrix.