from pytube import YouTube, Search
import telebot
from moviepy.editor import *

bot = telebot.TeleBot('6661761924:AAF1k5SWxmF50ZbaDgC3Z5PLC9D6DWSTJRE')


def download_mp3(url):

    my_video = YouTube(url)
    my_video = my_video.streams.get_audio_only()
    my_video.download()


s = Search(input("song name : "))

count = 0
for v in s.results:
    try:
        # print(f"{v.title}\n{v.watch_url}\n")
        if count == 0:
            download_mp3(v.watch_url)
            print(v.title)
    except:
        pass
    count += 1


