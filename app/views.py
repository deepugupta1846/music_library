from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


def index(request):
    msg = ""

    if request.method == 'POST':
        form = Insertform(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            msg = "Uploaded successfully"
        else:
            msg = "Failed!"
    form = Insertform()
    data = Music.objects.all()
    f = Music.objects.get(id=1)
    return render(request, 'index.html', {'data': data, 'form': form, 'msg': msg, 'f':f})


def delete(request, id):
    data = Music.objects.get(id=id)
    data.delete()
    return redirect('/')


def playMusic(request, id):
    song = Music.objects.get(id=id)
    msg = ""
    if request.method == 'POST':
        form = Insertform(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            msg = "Uploaded successfully"
        else:
            msg = "Failed!"
    form = Insertform()
    data = Music.objects.all()
    return render(request, 'playmusic.html', {'song':song, 'data': data, 'form': form, 'msg': msg})


def showDataById(request, id):
    d = Music.objects.get(id=id)
    dict = {'song': d.song.url, 'title': d.title, 'album': d.album.url}
    return JsonResponse(dict, safe=False)

