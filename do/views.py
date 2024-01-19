from django.shortcuts import render
from pytube import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        # link to get link of video
        link=request.POST["link"]
        a=request.POST["link"]
        video=YouTube(link)
        # download video in low resolution
        Stream=video.streams.get_lowest_resolution()
        #download video
        Stream.download()
        url=Stream.url
        return render(request, "home.html", {"a": url})
    return render(request, "home.html")

