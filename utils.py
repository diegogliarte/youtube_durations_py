import isodate as isodate

def get_playlist_videos(api, playlist_id):
    request = api.playlistItems().list(part="contentDetails",
                                       playlistId=playlist_id,
                                       maxResults=50)
    content = request.execute()
    playlist_videos = []
    for video in content["items"]:
        playlist_videos.append(video["contentDetails"]["videoId"])
    i = 0
    i += len(content["items"])
    while (content.get("nextPageToken") is not None):
        if i % 50 == 0:
            print(f"{i} videos requested")
        request = api.playlistItems().list(part="contentDetails",
                                           playlistId=playlist_id,
                                           pageToken=content["nextPageToken"],
                                           maxResults=50)
        content = request.execute()
        for video in content["items"]:
            playlist_videos.append(video["contentDetails"]["videoId"])
        i += len(content["items"])
    print(f"{i} videos requested\nRequesting completed\n")
    return playlist_videos

def parse_date (iso_date):
    return isodate.parse_duration(iso_date)

def get_video_duration(api, videos):
    duration = parse_date("PT0S")
    i = 0
    while len(videos) > 50:
        id_video = ",".join(videos[:50])
        duration += videos_limited_duration(api, id_video)
        videos = videos[50:]
        i += 50
        print(f"{i} durations processed")
    id_video = ",".join(videos)
    duration += videos_limited_duration(api, id_video)
    print(f"{i + len(videos)} durations processed\nDuration completed\n")

    return duration

def videos_limited_duration(api, id_video):
    duration = parse_date("PT0S")
    request = api.videos().list(id=id_video,
                                part="contentDetails")
    content = request.execute()
    for video in content["items"]:
        duration += parse_date(video["contentDetails"]["duration"])
    return duration

def get_playlist_url_from_channel_id(api, channel_id):
    request = api.channels().list(part="contentDetails",
                                  id=channel_id)

    return get_playlist_url_from(request)

def get_playlist_url_from_username(api, username):
    request = api.channels().list(part="contentDetails",
                                  forUsername=username)

    return get_playlist_url_from(request)

def get_playlist_url_from(request):
    content = request.execute()

    for items in content["items"]:
        channel_playlist_id = (items["contentDetails"]["relatedPlaylists"]["uploads"])

    return channel_playlist_id

def parse_url(url, argv):
    while url.count("list=") > 0:
        url = argv[argv.find("list=") + len("list="):]

    if url.count("&") > 0:
        url = url[:url.find("&")]
    return url


