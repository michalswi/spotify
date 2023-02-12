import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

CLIENT_ID = "todo"
CLIENT_SECRET = "todo"
PLAYLIST_LINK = "todo"

CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
SP = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)


def get_playlist_uri(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]

def get_tracks():
    dix = {
        "items": []
    }

    playlist_uri = get_playlist_uri(PLAYLIST_LINK)

    results = SP.playlist_tracks(playlist_uri)
    tracks = results["items"]
    while results["next"]:
        results = SP.next(results)
        tracks.extend(results['items'])
    
    trucksResults = tracks
    for track in range(0,len(trucksResults)):
        dix["items"].append({"id":track + 1,\
            "song":trucksResults[track]["track"]["name"],\
            "band":trucksResults[track]["track"]["artists"][0]["name"],\
            "album":trucksResults[track]["track"]["album"]["name"],
        })
    return dix

# get_tracks()
print(json.dumps(get_tracks()))
