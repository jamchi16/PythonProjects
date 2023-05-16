import os
import shutil
from moviepy.editor import VideoFileClip


def separate_long_mp4_files(directory, output_directory, duration_threshold=60):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                clip = VideoFileClip(file_path)
                duration = clip.duration
                clip.close()

                if duration > duration_threshold:
                    output_path = os.path.join(output_directory, file)
                    shutil.move(file_path, output_path)
                    print(f"Moved: {file_path} --> {output_path}")


directory_path = "C:/Users/james/OneDrive/Desktop/YoutubeClips"

output_directory_path = "C:/Users/james/OneDrive/Desktop/YoutubeClips/longvids"

separate_long_mp4_files(directory_path, output_directory_path)
