import os
from pytube import YouTube

# Replace the video link with your desired link
video_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object and get the highest resolution stream
yt = YouTube(video_link)
stream = yt.streams.get_highest_resolution()

# Replace the file path with your desired file path
output_folder = "./outputs/"

os.makedirs(output_folder)
# Download the video to the specified file path
stream.download(output_folder)