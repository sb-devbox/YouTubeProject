import sys
import os
from merge import merge_audio_video
from cs50 import get_string
from pytubefix import YouTube  # pytubefix used as regular pytube has an error

# Default test video
DEFAULT_VIDEO_URL = "https://www.youtube.com/shorts/WxF58hUZqX0"
itag_list = []

def main():

    # Handle optional -d flag
    if len(sys.argv) > 1 and "-d" in sys.argv:
        url = DEFAULT_VIDEO_URL
        print(f"Using default URL: {url}")
    else:
        #url = get_string("Video URL: ")  # Prompt user for input
        url = DEFAULT_VIDEO_URL

    # Generate a YouTube object
    video = get_video(url)

    # Print available streams
    print_streams(video)
    print(itag_list)
    # Collect user input for streams

    stream_itags = {
        "video": int(get_string("Video stream itag: ")),
        "audio": int(get_string("Audio stream itag: "))
    }
    
    # Download the selected streams
    print("Download Stream?")
    download_stream(video, stream_itags)


def get_video(url):
    """Returns a YouTube object from a URL."""
    return YouTube(url)


def print_streams(video):
    """Displays available video and audio streams."""
    video_streams = video.streams.filter(mime_type="video/mp4", only_video=True)
    audio_streams = video.streams.filter(mime_type="audio/mp4", only_audio=True).desc()

    print("\n##### VIDEO STREAMS #####")
    for index, stream in enumerate(video_streams):
        itag_list.append(video_streams.fmt_streams[index].itag)
        videos = video_streams.fmt_streams[index].itag
        print(stream)

    print("\n##### AUDIO STREAMS #####")
    for index, stream in enumerate(audio_streams):
        itag_list.append(audio_streams.fmt_streams[index].itag)
        audios = audio_streams.fmt_streams[index].itag
        print(stream)
    print(f"\nVideo Title: {video.title}")


def download_stream(video, itag):
    """Downloads the selected video and audio streams."""
    video_stream = video.streams.get_by_itag(itag["video"])
    audio_stream = video.streams.get_by_itag(itag["audio"])
    delete_flag = "-x" in sys.argv  # Check if '-x' flag is provided

    print(f"\nVideo Title: {video.title}")
    print(f"Video Filesize: {video_stream.filesize / 1_000_000_000:.4f} GB")
    print(f"Audio Filesize: {audio_stream.filesize / 1_000_000_000:.4f} GB")

    # Confirm before downloading
    user_input = get_string("Confirm download? (y/n): ").strip().lower()
    if user_input == "y":
        # Ensure correct file extensions
        video_file = "video.mp4"
        audio_file = "audio.mp3"

        video_stream.download(filename=video_file)
        audio_stream.download(filename=audio_file)

        print(f"✅ Download complete! Video saved as '{video_file}', Audio saved as '{audio_file}'")

        # Merge video and audio
        merge_audio_video(video_file, audio_file, (video.title + ".mp4"), delete_sources=delete_flag)
    else:
        print("❌ Download cancelled.")
        sys.exit(0)

if __name__ == "__main__":
    main()