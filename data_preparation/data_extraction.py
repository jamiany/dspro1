import spotipy
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials())
df = pd.read_csv(filepath_or_buffer='data.csv')


def get_tracks(playlist_name: str) -> pd.DataFrame:
    results = sp.playlist_items(playlist_name)

    track_ids = list(map(lambda song: song['track']['id'], results['items']))

    return df[df['id'].isin(track_ids)]

