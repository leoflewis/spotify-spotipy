import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
	name = ' '.join(sys.argv[1:])
	print(name)
else:
	sys.exit("no name given")	

results = spotify.search(q='artist:' + name, type='artist')
artist_id = results['artists']['items'][0]['id']
str_id = 'spotify:artist:'+artist_id
artist = spotify.artist(str_id)

print('Artist: ' + artist['name'])
print()
print('Artist top 10:')
artist_results = spotify.artist_top_tracks(str_id)
for track in artist_results['tracks']:
	print('-' + track['name'])
print()

print('Artist albums:')
artist_albums = spotify.artist_albums(str_id, album_type='album', country='US', offset=0, limit=50)
for album in artist_albums['items']:
	print('-' + album['name'])
print()

related_artists = spotify.artist_related_artists(str_id)
print('Related artists:')
for artist in related_artists['artists']:
	print('-' + artist['name'])
