from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = "https://www.youtube.com/live/tE2AcR2VpV8?si=CvwXa2LaPrnhSgnv"
Download(link)