from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Room

# rooms = [
#     {'id': 1, 'name': "Django"},
#     {'id': 2, 'name': "Python"},
#     {'id': 3, 'name': "AWS"}
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context )


def room(request,pk):

    room = Room.objects.get(id=int(pk))
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {"room":room}

    return render(request, 'base/room.html',context)