from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url: str):
    # extract video id safely
    if "v=" not in url:
        raise ValueError("Invalid YouTube URL")

    video_id = url.split("v=")[1].split("&")[0]
    print("Fetching transcript for video ID:", video_id)

    ytt_api = YouTubeTranscriptApi()   # create instance
    transcript = ytt_api.fetch(video_id)

    return " ".join([t.text for t in transcript])