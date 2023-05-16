import os
import shutil


def get_mp4_files(root_dir):
    mp4_files = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".mp4"):
                mp4_files.append(os.path.join(root, file))

    return mp4_files

root_directory = "D:/Nintendo"
output_directory = "C:/Users/james/OneDrive/Desktop/YoutubeClips"

mp4_files = get_mp4_files(root_directory)

for mp4_file in mp4_files:
    filename = os.path.basename(mp4_file)
    output_path = os.path.join(output_directory, filename)
    shutil.move(mp4_file, output_path)

print("All .mp4 files have been moved to the output directory.")
