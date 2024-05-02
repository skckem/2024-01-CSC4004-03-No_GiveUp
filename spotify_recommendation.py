from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

from matplotlib.image import imread
import matplotlib.pyplot as plt
import urllib.request

client_id = "0a3419c6f1934f9c85e6f0381335c2b0"
client_secret = "effc3df0867845fe8434dcb9a263c2bf"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist = "spotify:artist:6GwM5CHqhWXzG3l5kzRSAS"
artist_id = "6GwM5CHqhWXzG3l5kzRSAS"
image_save_loc = "./img.jpg"

#여기에 feature 추가
min_energy = 0.7
min_popularity = 50
min_tempo = 100

recommended = sp.recommendations(limit=3, market='KR', seed_artists=[artist], min_energy=min_energy, min_popularity=min_popularity, min_tempo=min_tempo)
tracks = recommended['tracks']
for track in tracks:
    song_url = track['external_urls']
    song_name = track['name']
    image_url = track['album']['images'][0]['url']
    urllib.request.urlretrieve(image_url, image_save_loc)
    image = imread(image_save_loc)

    print(song_url)
    print(song_name)
    plt.imshow(image)
    plt.show()

'''
Get Recommendation[’tracks’]의 자료구조
{'album': {
  'album_type': 'SINGLE', 
  'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5Q0U6ogBrMX2oxmxy5OTzU'}, 'href': 'https://api.spotify.com/v1/artists/5Q0U6ogBrMX2oxmxy5OTzU', 'id': '5Q0U6ogBrMX2oxmxy5OTzU', 'name': 'SISTAR19', 'type': 'artist', 'uri': 'spotify:artist:5Q0U6ogBrMX2oxmxy5OTzU'}], 
  'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 
  'external_urls': {'spotify': 'https://open.spotify.com/album/7Jxv3EPhYBh6zevT4eUZQo'}, 
  'href': 'https://api.spotify.com/v1/albums/7Jxv3EPhYBh6zevT4eUZQo', 
  'id': '7Jxv3EPhYBh6zevT4eUZQo', 
  'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273364f8ae58ec2a85d61b941f4', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02364f8ae58ec2a85d61b941f4', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851364f8ae58ec2a85d61b941f4', 'width': 64}], 
  'name': 'Gone not around any longer', 
  'release_date': '2013-01-31', 
  'release_date_precision': 'day', 
  'total_tracks': 5, 
  'type': 'album', 
  'uri': 'spotify:album:7Jxv3EPhYBh6zevT4eUZQo'
  }, 
  'artists': [
    {'external_urls': {'spotify': 'https://open.spotify.com/artist/5Q0U6ogBrMX2oxmxy5OTzU'}, 
     'href': 'https://api.spotify.com/v1/artists/5Q0U6ogBrMX2oxmxy5OTzU', 
     'id': '5Q0U6ogBrMX2oxmxy5OTzU', 
     'name': 'SISTAR19', 
     'type': 'artist', 
     'uri': 'spotify:artist:5Q0U6ogBrMX2oxmxy5OTzU'}
  ], 
  'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 
  'disc_number': 1, 
  'duration_ms': 211069, 
  'explicit': False, 
  'external_ids': {'isrc': 'KRA381202681'}, 
  'external_urls': {'spotify': 'https://open.spotify.com/track/4TAENzBN2lYuXBF9ZNauwJ'}, 
  'href': 'https://api.spotify.com/v1/tracks/4TAENzBN2lYuXBF9ZNauwJ', 
  'id': '4TAENzBN2lYuXBF9ZNauwJ', 
  'is_local': False, 
  'name': 'Gone not around any longer', 
  'popularity': 50, 
  'preview_url': 'https://p.scdn.co/mp3-preview/6c8ed3ca393ea0085e8a1954b5ffbbb094bc485e?cid=0a3419c6f1934f9c85e6f0381335c2b0', 
  'track_number': 2, 
  'type': 'track', 
  'uri': 'spotify:track:4TAENzBN2lYuXBF9ZNauwJ'
}

'''