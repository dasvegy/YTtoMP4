from pytube import YouTube

yt = YouTube(str(input("Link 🔫 \n-> ")))
video = yt.streams.get_highest_resolution()
video.download()

print("Video:" + yt.title + "Downloaded Successfully")
