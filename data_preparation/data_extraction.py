import spotipy
from dotenv import load_dotenv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from data_preparation.expections import test_set

load_dotenv()

df = pd.read_csv(filepath_or_buffer='data.csv', sep=',', index_col=0)
df.drop(df.loc[df['id'].isnull()].index, inplace=True)


def get_tracks(playlist_name: str, sp=None, test=False) -> pd.DataFrame:
    if sp is None:
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials())

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
            'release_year': track['album']['release_date'].split('-')[0],
        }

        df_tracks.loc[df_tracks['id'] == track['id'], track_data.keys()] = track_data.values()

    scale_release_year(df_tracks)

    # add expected labels during testing
    if test:
        if playlist_name == '5Rh7ikX5dteMXfc8tmeBJy':
            df_expected_label = pd.DataFrame(test_set.items(), columns=['id', 'expected_label'])
        else:
            raise ValueError('no expected labels were found')

        df_tracks = df_tracks.merge(df_expected_label, on='id', how='left')

    return df_tracks


def scale_release_year(df):
    df_release_year = df['release_year'].to_frame()

    scaler = MinMaxScaler()
    scaler.fit(df_release_year)

    # adjust the scaling of the release year to be between 1950 and 2025
    min_year = 1925
    max_year = 2025

    year_range = max_year - min_year
    scaler.scale_[0] = 1 / year_range
    scaler.min_[0] = -min_year / year_range

    df['release_year'] = scaler.transform(df_release_year)

