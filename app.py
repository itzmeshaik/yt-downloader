from pytube import YouTube

url = input("Enter the full url of the video you want to download: ")

audioYes = input("Do you only want the audio?(Y/N): ")

yt = YouTube(url)

if audioYes.lower() == 'y':
    print("Downloading audio of:", yt.title)
    audioStream = yt.streams.filter(only_audio=True).first()
    audioStream.download()
    print("Audio download complete!")

elif audioYes.lower() == 'n':
    print("Download video:", yt.title)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download complete.")

else:
    print('run the program again and enter a valid input.')
