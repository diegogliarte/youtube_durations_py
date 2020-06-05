import isodate as isodate

def get_playlist_videos(api, playlist_id):
    request = api.playlistItems().list(part="contentDetails", playlistId=playlist_id)
    content = request.execute()
    playlist_videos = []
    for video in content["items"]:
        playlist_videos.append(video["contentDetails"]["videoId"])

    while (content.get("nextPageToken") is not None):
        request = api.playlistItems().list(part="contentDetails", playlistId=playlist_id,
                                           pageToken=content["nextPageToken"])
        content = request.execute()
        for video in content["items"]:
            playlist_videos.append(video["contentDetails"]["videoId"])
    return playlist_videos

def parse_date (iso_date):
    return isodate.parse_duration(iso_date)

def get_video_duration(api, videos):
    id_video = ",".join(videos)
    request = api.videos().list(id=id_video, part="contentDetails")
    content = request.execute()
    duration = parse_date("PT0S")
    for video in content["items"]:
        duration += parse_date(video["contentDetails"]["duration"])
        print(video)
    return duration


