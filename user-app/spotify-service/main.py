import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import spotipy
import random
from spotipy.oauth2 import SpotifyOAuth

app = FastAPI()
sp_oauth = SpotifyOAuth(
    client_id="cf78bb1275bd4529a8678b9bada05c3a",
    client_secret="5bd5e4fed3d74d3196f634a71320b1cb",
    redirect_uri="http://127.0.0.1:8000/api/callback",
    scope="user-library-read playlist-modify-private"
)

session = {}

@app.get("/api/login")
async def login():
    auth_url = sp_oauth.get_authorize_url()
    session["token_info"] = sp_oauth.get_cached_token()
    return RedirectResponse(auth_url)

@app.get("/api/callback")
async def callback(code):
    token_info = sp_oauth.get_access_token(code)
    print(token_info)
    print(session)
    session["token_info", token_info]
    # return RedirectResponse("/generate")  # Redirect to app's main page


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # only for debugging