from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn programming'},
    {'id': 2, 'name': 'Design UI/UX with me'},
    {'id': 3, 'name': 'Frontend Developer'},
    {'id': 4, 'name': 'Backend Developer'},
]


def index(request):
    context = {'rooms': rooms}
    return render(request, 'website/index.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'website/room.html', context)