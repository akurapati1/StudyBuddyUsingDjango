from django.shortcuts import render
# Create your views here.


rooms = [
    {'id' :1, 'name': "Lets learn Django"},
    {'id' :2, 'name': "Lets learn Sprintgboot"},
    {'id' :3, 'name': "Lets learn Gen AI"},
]
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'room.html')
