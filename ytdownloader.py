import tkinter as tk
from pytube import YouTube
from tkinter import *

root= tk.Tk()

root.title('YouTube Downloader')
canvas1 = tk.Canvas(root, width = 500, height = 280,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Download from Youtube')
label1.config(font=('helvetica', 14))
canvas1.create_window(250, 25, window=label1)

label2 = tk.Label(root, text='Please input your link')
label2.config(font=(10))
canvas1.create_window(250, 100, window=label2)

entry1 = tk.Entry (root)
entry1.config(font=('helvetica', 12))
canvas1.create_window(250, 140, width=400, height =30, window=entry1)


def download_audio():
    link = entry1.get()
    video = YouTube(link)
    video.streams.get_audio_only().download('Downloads/Audio', video.title + '.mp3')
    label4 = tk.Label(root, text='Utwór ' + video.title + ' został pobrany!')
    label4.config(font=('helvetica', 10))
    canvas1.create_window(250, 250, window=label4)

def download_video():
    link = entry1.get()
    video = YouTube(link)
    video.streams.get_highest_resolution().download('Downloads/Video')
    label4 = tk.Label(root, text='Film ' + video.title + ' został pobrany!')
    label4.config(font=('helvetica', 10))
    canvas1.create_window(250, 250, window=label4)



button1 = tk.Button(text='Download Audio', command=download_audio, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(170, 190, width=150, window=button1)

button2 = tk.Button(text='Download Video', command=download_video, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(330, 190, width=150, window=button2)


root.mainloop()
