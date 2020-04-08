import pytube
video_urls = ['https://www.youtube.com/watch?v=KFvb_mluq8Y',
		'https://www.youtube.com/watch?v=w-9i3hxmBso', 
'https://www.youtube.com/watch?v=xRW_t7XAenk', 
'https://www.youtube.com/watch?v=StGm-m1EUgk', 
'https://www.youtube.com/watch?v=8vWaawiUteM']
for video_url in video_urls:
	youtube = pytube.YouTube(video_url)
	video = youtube.streams.first()
	video.download('../') # path, where to video download.