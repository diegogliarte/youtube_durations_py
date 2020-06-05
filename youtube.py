import google_auth_oauthlib.flow
import googleapiclient.discovery as gapi
import time
from sys import argv

from utils import *

if (len(argv) != 2):
    print("Invalid format")
    exit(1)

url = argv[1][argv[1].find("=") + 1:][argv[1][argv[1].find("=") + 1:].find("=") + 1:]

api_key = "ERROR" # Use your key
api_service_name = "youtube"
api_version = "v3"
playlist_id = url

if api_key is "ERROR":
    print("Use your own API KEY")
    exit(1)

api = gapi.build(api_service_name, api_version, developerKey=api_key)

videos = get_playlist_videos(api, playlist_id)
duration = get_video_duration(api, videos)

print(duration)







