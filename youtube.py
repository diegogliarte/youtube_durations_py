import googleapiclient.discovery as gapi
from sys import argv
from utils import *
import os

# if len(argv) != 2:
#     print("Invalid format")
#     exit(1)
api_key = os.environ.get("API_YOUTUBE_KEY")
api_service_name = "youtube"
api_version = "v3"


def youtube_duration(url_argv):
    if api_key == "ERROR":
        print("Use your own API KEY")
        exit(1)

    api = gapi.build(api_service_name, api_version, developerKey=api_key)

    # You can either use a channel ID to get all the videos duration, or a playlist to get the playlist duration
    url = parse_url(url_argv)
    print(url)
    try:  # Is it from username?
        url = get_playlist_url_from_username(api, url)
    except:
        try:  # Is it from channel id?
            url = get_playlist_url_from_channel_id(api, url)
        except:
            pass

    try:
        print("Requesting videos...")
        videos = get_playlist_videos(api, url)
        if videos == -1:
            return videos, 0

        print("Processing videos duration...")
        duration, total_videos = get_video_duration(api, videos)

        return duration, total_videos

    except:
        return "error", 0
