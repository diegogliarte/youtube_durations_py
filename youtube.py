import googleapiclient.discovery as gapi
from sys import argv
from utils import *

# if len(argv) != 2:
#     print("Invalid format")
#     exit(1)

def youtube_duration(url_argv):
    api_key = "AIzaSyBPhY0mogI7Yfdasr427NBjfgb3ay0jDAg"
    api_service_name = "youtube"
    api_version = "v3"

    if api_key == "ERROR":
        print("Use your own API KEY")
        exit(1)

    api = gapi.build(api_service_name, api_version, developerKey=api_key)

    url = url_argv
    #You can either use a channel ID to get all the videos duration, or a playlist to get the playlist duration
    try:
        url = get_playlist_url_from_channel_id(api, url)
    except:
        try:
            url = get_playlist_url_from_username(api, url)
        except:
            url = parse_url(url, url_argv)

    try:
        print("Requesting videos...")
        videos = get_playlist_videos(api, url)
        print("Processing videos duration...")
        duration = get_video_duration(api, videos)
    except:
        duration = "error"

    return duration

