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
    video = YouTube(url)
    title = video.title
    streams = get_streams(video)
    print_streams(streams)


    #select av_streams for download
    selected_streams= {}
    for stream_type, stream_list in streams.items():
        while True:
            user_input = int(get_string(f"{stream_type.capitalize()} stream itag: "))
            if user_input in stream_list.itag_index.keys():
                break
            else:
                print(f"Please enter a valid {stream_type} stream itag")
        selected_streams[stream_type] = streams[stream_type].get_by_itag(user_input)

    
    #confirm & download av_stream
    print(f"\n{title}")
    print_size(selected_streams) 
    user_input = get_string("Confirm download? (y/n): ").strip().lower()
    file = []
    if user_input == "y":
        for stream_type, stream_item in selected_streams.items():
            stream = selected_streams[stream_type]
            file_name = stream_type + "." + selected_streams[stream_type].subtype
            file.append(download_stream(stream, file_name))
            print(f"✅ Download completed saved as {file_name}.")
    else:
        print("❌ Download cancelled.")
        sys.exit(1)

    #merge videos via
    if len(file) == 2:
        merge_audio_video(file[0], file[1], title)
    else:
        sys.exit(1)
    

#gets streams from YouTube object
def get_streams(video):
    stream = video.streams
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


def print_size(streams):
    for stream_type, stream_list in streams.items():
        print(f"{stream_type.capitalize()} Filesize: {stream_list.filesize / 1_000_000_000:.4f} GB")


def download_stream(stream, file_name):
    stream.download(filename=file_name)
    return file_name

if __name__ == "__main__":
    main()