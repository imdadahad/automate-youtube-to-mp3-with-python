# %%
import subprocess
import youtube_dl
import os

# %%


def run():
    # Ask the user for the video they want to download
    video_url = input("Please enter the YouTube Video URL: ")
    # Download and convert to mp3 and store in downloads folder
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False)

    video_title = video_info['title']
    filename = f"{video_title}.mp3"

    # Ask the user for the path they want to save the file after it has been downloaded
    path_to_save = input(
        r"Enter where the file is to be saved or leave empty if you want it to be saved in the current working directory: "
    )

    where_to_save = os.getcwd()

    if path_to_save != "":
        where_to_save = f"{path_to_save}"

    filename = f"{video_info['title']}.mp3"
    output_path = os.path.join(where_to_save, filename)

    options_bin = input(
        "Enter 1 for audio only, 2 for video only or 3 for both: ")

    class Download_Options:
        def __init__(self, options_bin):
            #self.media_type = media_type
            self.options_bin = options_bin
            #self.target_media = target_media
            self.video_target = {
                "noplaylist": True,
                "quiet": True,
                "format": "bestvideo",
            }
            self.audio_target = {
                # reduces the several line of output to barest minimal and therefore, time
                'quiet': True,
                'noplaylist': True,
                'format': 'bestaudio/best',
                'keepvideo': True,
                'outtmpl': output_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }

        def download_media(self, video_info):
            """
            docstring
            """
            if self.options_bin == "1":
                with youtube_dl.YoutubeDL(self.audio_target) as ydl:
                    ydl.download([video_info['webpage_url']])

            elif self.options_bin == '2':
                with youtube_dl.YoutubeDL(self.video_target) as ydl:
                    ydl.download([video_info['webpage_url']])

            elif self.options_bin == '3':
                for each_item in [self.audio_target, self.video_target]:
                    with youtube_dl.YoutubeDL(each_item) as ydl:
                        ydl.download([video_info['webpage_url']])

    audio_media_type = Download_Options(options_bin)
    audio_media_type.download_media(video_info)

    # # returns os system eg. 'nt' for windows
    coding_env = os.name

    # # Open the file once it has been downloaded
    os.startfile(filename) if coding_env == 'nt' else subprocess.call(
        ["open", filename])


if __name__ == '__main__':
    run()
