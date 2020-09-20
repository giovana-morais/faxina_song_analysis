import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pp = pprint.PrettyPrinter(indent=2)

def login():
    auth_manager=SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


def search(sp, query_str, limit):
    results = sp.search(q=query_str, limit=limit, type='playlist')
    pp.pprint(results)
    # for idx, track in enumerate(results['tracks']['items']):
    #     print(idx, track['name'])

if __name__ == '__main__':
    sp = login()

    search(sp, 'faxina', 1)
