from django.shortcuts import render
from pytube import *
def index(request):
        return render(request, 'index.html')
def youtube(request):
    if request.method=="POST":
        link=request.POST["link"]
        video = YouTube(link)
        stream = video.streams.get_lowest_resolution()
        stream.download()
        return render(request,"index.html")
    return render(request, "index.html")
    
