'''
YouTube video or audio downloader using command line input
-by Mohammed Saad
Credits: https://pypi.org/project/pytube/
Installation: pip install pytube
'''

from pytube import YouTube
from pyfiglet import Figlet  # Intro text
from clint.textui import puts, colored, indent, progress  # Colored text
from clint.arguments import Args
from terminaltables import SingleTable  # Table view

global MaxFileSize, fileSizeInBytes

f = Figlet(font='slant')
inroText = f.renderText('YT Downloader')
print(inroText)

link = input(colored.green('Enter link to download: '))
print()


def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # Gets the percentage of the file that has been downloaded.
    percent = (100 * (fileSizeInBytes - remaining)) / fileSizeInBytes
    print("\r{:00.0f}% downloaded".format(percent), end='')


# creating object of class YouTube @param video link @param download progress status
youtube = YouTube(link, on_progress_callback=progress)

print(colored.yellow("\tSELECT THE FORMAT TO DOWNLOAD"))
table_data = [
    ['Format ID', 'VIDEO', '', 'Format ID', 'AUDIO'],
    ['1', '1080p', ' ', '4', '128kbps'],
    ['2', '720p', ' ', '5', '70kbps'],
    ['3', '480p', ' ', '6', '50kbps']
]
table = SingleTable(table_data)
print(colored.cyan(table.table))

downloadType = input(colored.green('Enter format id: '))
print()
# checking if the input entered is int
try:
    val = int(downloadType)
    if val == 1:
        selectedVideo = youtube.streams.get_by_itag(137)
    elif val == 2:
        selectedVideo = youtube.streams.get_by_itag(22)
    elif val == 3:
        selectedVideo = youtube.streams.get_by_itag(135)
    elif val == 4:
        selectedVideo = youtube.streams.get_by_itag(140)
    elif val == 5:
        selectedVideo = youtube.streams.get_by_itag(250)
    elif val == 6:
        selectedVideo = youtube.streams.get_by_itag(249)
except ValueError:
    print(colored.red('INVALID INPUT'))
    exit()


print(colored.yellow('Title = ' + youtube.title))
fileSizeInBytes = selectedVideo.filesize
MaxFileSize = fileSizeInBytes/1024000
MB = str(MaxFileSize) + " MB"
print(colored.yellow("File Size = {:00.00f} MB".format(MaxFileSize)))

selectedVideo.download()

print(colored.green('\rVIDEO DOWNLOADED!!'))
