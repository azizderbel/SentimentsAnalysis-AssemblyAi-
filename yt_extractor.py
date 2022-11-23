import youtube_dl

ydl = youtube_dl.YoutubeDL()

def get_video(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )
    if "entries" in result:
        return result["entries"][0]
    return result

def get_audio_url(video_info): 
    for f in video_info["formats"]:
        if f['ext'] == 'm4a':
            return f['url']



