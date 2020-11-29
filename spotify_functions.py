import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pp = pprint.PrettyPrinter(indent=2)

def login():
    auth_manager=SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


def top_10_playlists(sp, query_str, limit):
    results = sp.search(q=query_str, limit=limit, type='playlist')
    # pp.pprint(results)
    playlists = results['playlists']['items']
    details = playlists[0].keys()
    print(details)
    for playlist_details in playlists:
        tracks = sp.playlist(playlist_details['id'], fields="tracks")
        print(tracks)
        input("continuar ")

if __name__ == '__main__':
    sp = login()

    top_10_playlists(sp, 'faxina', 1)
