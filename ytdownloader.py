from pytube import YouTube
import time

while True:
    link = input('Please input a youtube video link ')
    video = YouTube(link)
    print('Video title: ', video.title)

    type = input('Do you want to download audio or video? Type: 1 - audio / 2- video ')

    if type == '1':
        time.sleep(1)
        print('Please wait till your download is complete!')
        video.streams.get_audio_only().download('Downloads/Audio', video.title + '.mp3')
        print(video.title, " audio has been successfully downloaded.")
    elif type == '2':
        time.sleep(1)
        print('Please wait till your download is complete!')
        video.streams.get_highest_resolution().download('Downloads/Video')
        print(video.title, " video has been successfully downloaded.")
    else:
        print('Try Again')