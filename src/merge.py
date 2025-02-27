import ffmpeg
import os

def merge_audio_video(video_file, audio_file, output_file, delete_sources=True):
    try:
        # Separate input calls for video and audio
        video = ffmpeg.input(video_file)  # Video input
        audio = ffmpeg.input(audio_file)  # Audio input

        # Merge video and audio
        (
            ffmpeg
            .output(video, audio, output_file+".mp4", vcodec="copy", acodec="aac")  # Corrected order
            .run(overwrite_output=True)
        )
        print(f"✅ Merged successfully: {output_file}")

        if delete_sources:
            os.remove(video_file)
            os.remove(audio_file)
            print("🗑️  Deleted source files.")
        else:
            print("🖇️  Source files retained.")
            print("WARNING!! Source files will be overwritten if another video is downloaded!")

    except ffmpeg.Error as e:
        print("❌ FFmpeg error:", e.stderr.decode())
