import yt_dlp

url = input("enter the full url of the video you want to download: ")

type = input("do you only want to download the audio of the video(y/n)?:")
try:
    if type.lower == "y":
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{"key": "FFmpegExtractAudio"}],
        }
    else:
        ydl_opts = {
            "format": "bestaudio+bestvideo",
            "merge_output_format": "mp4",
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

except yt_dlp.utils.DownloadError:
    print("there was an error in downloading the video. Try Again")

except KeyboardInterrupt:
    print("Bye!👋")

else:
    print("downloading successful.")

finally:
    print("execution complete.")
