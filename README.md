# Smart Playlist (Spotify Song Clustering)

Data Science Project 1 HSLU AI/ML

## Autohrs

Jamian Rajakone and Tamino Walter

## Short Description

Our project aims to develop a Spotify song clustering system. The goal is to take a playlist of randomly selected songs and intelligently group them based on their similarities. This would allow users to easily organize and discover patterns in their playlists. The idea is to select a representative song for each cluster, using it as a basis to separate or categorize the rest of the songs within the playlist.

Data: https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs

## Getting Started

*Data Engineering part*

Execute the Python Notebooks in following order:

1. data_collection.ipynb
2. data_exploration.ipynb
3. data_extraction.ipynb
4. clustering.ipynb

The generated data.csv should be copied to the backend service folder (user-app/spotify-service)

> Don't use *_2.ipynb: created only for testing purpose

*Real World Application*

User Application is under user-app separated in spotify-cluster (frontend: react UI) and spotify-service (backend: python fastapi)

## User Interface

Link to mockup (Figma): https://www.figma.com/design/IhWmeorig6KSzmQKxUacmb/Spotify-Smart-Playlist?node-id=1-30&t=lOsyOzdGZmqjgHka-1
