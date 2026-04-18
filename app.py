import yt_dlp

url = input("enter the full url of the video you want to download: ")

type = input("do you only want to download the audio of the video(y/n)?:")

if type.lower == 'y':
    ydl_opts = {
            'format':'bestaudio/best',
            'postprocessors': [{
                'key':'FFmpegExtractAudio'
                }],
    }
else:
    ydl_opts = {
            'format': 'bestaudio+bestvideo',
            'merge_output_format': 'mp4',
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
