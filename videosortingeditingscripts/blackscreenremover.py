import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def remove_black_screens(input_directory, output_directory, threshold=0.98, min_duration=1):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".mp4"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_directory, file)

                video_clip = VideoFileClip(input_file)

                # Iterate through each frame to detect black screen sections
                black_screens = []
                duration = 0
                for frame in video_clip.iter_frames():
                    is_black = frame.mean() < threshold

                    if is_black:
                        duration += 1 / video_clip.fps
                    elif duration > 0:
                        if duration >= min_duration:
                            black_screens.append((duration, duration + video_clip.duration))
                        duration = 0

                # Cut out black screen sections and generate the final video clip
                final_clips = []
                start_time = 0
                for start, end in black_screens:
                    if start_time < video_clip.duration:
                        final_clips.append(video_clip.subclip(start_time, start))
                    start_time = end

                if start_time < video_clip.duration:
                    final_clips.append(video_clip.subclip(start_time))

                final_video = concatenate_videoclips(final_clips)

                # Write the final video to the output file
                final_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

                video_clip.close()
                final_video.close()

                print(f"Black screens removed: {input_file} --> {output_file}")


# Provide the directory path where the input .mp4 files are located
input_directory_path = "C:/Users/james/OneDrive/Desktop/YoutubeClips/shortvids"

# Provide the directory path where the output processed files will be saved
output_directory_path = "C:/Users/james/OneDrive/Desktop/YoutubeClips/ready"

# Specify the threshold for black screen detection (0.0 - 1.0, default is 0.98)
black_screen_threshold = 0.98

# Specify the minimum duration of black screen to be removed (in seconds, default is 1)
minimum_black_screen_duration = 1

# Remove black screen sections from all .mp4 files in the directory
remove_black_screens(input_directory_path, output_directory_path, black_screen_threshold, minimum_black_screen_duration)
