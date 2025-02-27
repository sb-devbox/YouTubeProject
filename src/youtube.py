import sys
import os
from merge import merge_audio_video
from cs50 import get_int
from cs50 import get_string
from pytubefix import YouTube  # pytubefix used as regular pytube has an error

# Default test video
DEFAULT_VIDEO_URL = "https://www.youtube.com/shorts/WxF58hUZqX0"

def main():

    # -d flag, auto select default video
    if len(sys.argv) > 1 and "-d" in sys.argv:
        url = DEFAULT_VIDEO_URL
        print(f"Using default URL: {url}")
    else:
        url = DEFAULT_VIDEO_URL



    #basic program flow
    streams = get_streams(url)
    print_streams(streams)

    selected_streams= {}
    for stream_type, stream_list in streams.items():
        selected_streams = get_string(f"{stream_type.capitalize()} stream itag: ")
        download_list[stream_type] = streams[stream_type].get_by_itag(user_input)

    print("Download Stream?")
    print(download_list)

    
    download_stream(download_list)

    # Download the selected streams
    
    #download_stream(video, stream_itags)


































#gets streams from YouTube object
def get_streams(url):
    stream = YouTube(url).streams
    streams = {
        "video":stream.filter(mime_type="video/mp4", only_video=True),
        "audio":stream.filter(mime_type="audio/mp4", only_audio=True)
    }
    return streams

def print_streams(streams):
    for stream_type, stream_list in streams.items():
        print(f"\n##### {stream_type.upper()} STREAMS #####")
        for stream in stream_list:
            print(stream)
    #print(f"\nVideo Title: {video.title}")

def download_streams(streams):
    for stream_type, stream_list in streams.items():
       print(f"{stream_type.capitalize} Filesize: {filesize / 1_000_000_000:.4f} GB") 
    
    user_input = get_string("Confirm download? (y/n): ").strip().lower()
    if user_input == "y":

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











def download_stream(streams, itag):

    for stream_type, stream_list in streams.items():
        
        print(f"{stream_type} Filesize: {stream_list.filesize / 1_000_000_000:.4f} GB")



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