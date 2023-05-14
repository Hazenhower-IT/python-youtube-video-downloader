from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('C:\Downloads')

# Istruzioni: aprire il terminale e digitare es: python main.py "https://www.youtube.com/UrlDelVideoCheVuoiScaricare"
# Il Video Verra Scaricato nella cartella Downloads del proprio pc