# THIS IS THE VERSION WITH THE VERIFICATION OF THREE DOWNLOADED VIDEOS
# VERIFICATION BRANCH

from pytube import YouTube
from pytube import Playlist
import math
import os
import click

# INSERT THE PLAYLIST LINK OF THE CHANNEL
channel = input("URL of the channel you want to download all the audios(Playlist Link): ")
count = 0
exceptionsCount = 0

def AudioDownload(video_link, destination, amount):
    audios = YouTube(video_link)

    audio = audios.streams.filter(only_audio=True).first()

    out_file = audio.download(output_path=destination)

    # conversion to mp3 file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    global exceptionsCount
    try:
        os.rename(out_file, new_file)

    except FileExistsError:
        os.remove(out_file)
        exceptionsCount = exceptionsCount+1

    global count
    count = count + 1

    # function to display progress
    progress(count, amount)

    return exceptionsCount

def DownloadChannel(channel_link):
    list_videos = Playlist(channel_link)
    DownloadChannel.amount = len(list_videos)
    # choose the directory you want to download the files
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or "."

    for url in list_videos:
        verification = AudioDownload(url, destination, DownloadChannel.amount)
        if verification >=3:

            #function to clear the screen
            click.clear()
            print("The rest of the audios are already downloaded!\n")
            break

    #RENAME FILES WITH PREFIX


def progress(count, amount):
    # width of the progress bar
    progress.width = 40;
    percent=count/amount
    left = math.ceil(progress.width * (percent))
    right = progress.width - left
    tags = '#' * left
    spaces = " " * right
    percents = f"{(percent*100):.0f}%"
    print(" Downloaded: ", count, "/", amount, ". Progress: [",tags,spaces,"]", percents,"\r", end="")


DownloadChannel(channel)

CompleteProgress = '#' * progress.width
print("All the audios were downloaded!. Progress: ",DownloadChannel.amount,"/",DownloadChannel.amount," [",CompleteProgress,"] 100% ", end="")
