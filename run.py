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

    options = {
        # reduces the several line of output to barest minimal and therefore, time
        'quiet':
        True,
        'format':
        'bestaudio/best',
        'keepvideo':
        False,
        # f"{where_to_save}\\{filename}"
        'outtmpl':
        os.path.join(where_to_save, filename),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    filename = f"{video_info['title']}.mp3"

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    # returns os system eg. 'nt' for windows
    coding_env = os.name

    # Open the file once it has been downloaded
    os.startfile(filename) if coding_env == 'nt' else subprocess.call(
        ["open", filename])


if __name__ == '__main__':
    run()

# %%
