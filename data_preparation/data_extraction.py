import spotipy
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials())
df = pd.read_csv(filepath_or_buffer='data.csv', sep=',', index_col=0)
df.drop(df.tail(1).index, inplace=True)


def get_tracks(playlist_name: str, spotify = None) -> pd.DataFrame:
    if spotify is not None:
        sp = spotify
    # get the tracks from spotify
    results = sp.playlist_items(playlist_name)

    track_ids = list(map(lambda song: song['track']['id'], results['items']))

    # get the dataframe with track and feature data from our stored dataset
    df_tracks = df[df['id'].isin(track_ids)]

    # cleanup track data with potential null values
    for item in results['items']:
        track = item['track']

        track_data = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
        }

        df_tracks.loc[df_tracks['id'] == track['id'], track_data.keys()] = track_data.values()

    return df_tracks

