import os
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.AudioClip import CompositeAudioClip

def add_audio_to_video(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path).subclip(0, video.duration)
    original_audio = video.audio
    adjusted_audio = audio.volumex(0.5)
    final_audio = CompositeAudioClip([original_audio, adjusted_audio])
    final_video = video.set_audio(final_audio)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

directory = "C:/Users/james/OneDrive/Desktop/YoutubeClips/shortvids"

for file_name in os.listdir(directory):
    if file_name.endswith(".mp4"):
        video_path = os.path.join(directory, file_name)
        audio_path = os.path.join(directory, "music.mp3")  # Change the audio file name accordingly
        output_path = os.path.join(directory, "output1_" + file_name)  # Output video file name
        add_audio_to_video(video_path, audio_path, output_path)







