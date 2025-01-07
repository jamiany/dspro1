import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

import spotipy
import random
from spotipy.oauth2 import SpotifyOAuth
from sklearn import cluster
import numpy as np

from dspro1.data_preparation.data_extraction import get_tracks

app = FastAPI() #start with `fastapi dev main.py`

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sp_oauth = SpotifyOAuth(
    client_id="cf78bb1275bd4529a8678b9bada05c3a",
    client_secret="5bd5e4fed3d74d3196f634a71320b1cb",
    redirect_uri="http://127.0.0.1:8000/api/callback",
    scope="user-library-read playlist-read-private playlist-read-collaborative"
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

session = {}

@app.get("/api/login")
async def login():
    auth_url = sp_oauth.get_authorize_url()
    session["token_info"] = sp_oauth.get_cached_token()
    return RedirectResponse(auth_url)

@app.get("/api/callback")
async def callback(code):
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = sp_oauth.get_cached_token()
    return RedirectResponse("http://localhost:3000/start")

@app.get("/api/playlist")
async def playlist():
    return sp.current_user_playlists()

@app.post("/api/startclustering/{id}/{clusters}")
async def start_cluster(id, clusters):
    df = get_tracks(id, sp)
    df_features = df.drop(columns=['id', 'name', 'artist', 'album', 'release_year'])

    labels = None
    number_of_clusters = int(clusters)
    if number_of_clusters < 2:
        labels = _auto_cluster_songs(df_features).labels_.tolist()
    else:
        labels = _cluster_songs(number_of_clusters, df_features).labels_.tolist()

    result = {}
    for unique_label in set(labels):
        result[unique_label] = []

    for i, label in enumerate(labels):
        result[label].append({
            'id': df.iloc[i]['id'],
            'group': label,
            'name': df.iloc[i]['name'],
            'album': df.iloc[i]['album'],
            'artist': df.iloc[i]['artist'],
        })

    return result

def _cluster_songs(k_parameter, df_features):
    max_num_cluster = min(df_features.shape[0], k_parameter)
    model = cluster.KMeans(
        n_clusters=max_num_cluster,
        max_iter=900,
        random_state=53,
    )
    model.fit(df_features)
    return model

def _auto_cluster_songs(df_features):
    wcss = []
    dict = {}
    max_num_clusters = min(df_features.shape[0], 11)
    for i in range(2, max_num_clusters):  # Testing cluster numbers from 1 to 10
        kmeans = _cluster_songs(i, df_features)
        wcss.append(kmeans.inertia_)
        dict[i] = kmeans
    
    optimal_clusters = np.diff(wcss, 2).argmin() + 2
    return dict[optimal_clusters]
    
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # only for debugging