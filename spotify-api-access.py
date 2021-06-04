import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
	name = ' '.join(sys.argv[1:])
	print(name)
else:
	sys.exit("no name given")	

results = spotify.search(q='artist:' + name, type='artist')
artist_id = results['artists']['items'][0]['id']
str_id = 'spotify:artist:'+artist_id
artist_results = spotify.artist_top_tracks(str_id)
for track in artist_results['tracks']:
	print(track['name'])

