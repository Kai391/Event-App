from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Event
import json
# Create your views here.

# Home page
def index(request):
    events=Event.objects.all()
    return render(request,"index.html",{'events':events})

# Likes Page
def likes(request):
    likes=Event.objects.filter(Is_Liked=True)
    return render(request,"Likes.html",{'events':likes})

# Createing events
def createEvent(request):
    if request.method =="POST":
        # name Date time location image
        name = request.POST.get("name")
        date = request.POST.get("Date")
        time = request.POST.get("time")
        location = request.POST.get("location")
        image=request.FILES['image']
        # print("Image:",request.FILES["image"])
        Event(Name=name,Date=date,Time=time,Location=location,Image=image).save()
    return render(request,"Event.html")

# AJAX call for Like an event
def liking(request):
    data = json.loads(request.body)
    # print(data)
    dt=Event.objects.get(id=data["eventId"])
    if dt.Is_Liked == True:
        dt.Is_Liked=False
    else:
        dt.Is_Liked=True
    dt.save()
    newData = {"eventColor":dt.Is_Liked,"eventId":data["eventId"]}
    # print(newData)
    return JsonResponse(newData,safe=False)