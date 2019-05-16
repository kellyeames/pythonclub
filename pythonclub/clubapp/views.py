from django.shortcuts import render, get_object_or_404
from .models import Event, MeetingMinutes, Meeting, Resource

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html', {'resource_list' : resource_list})

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html', {'meeting_list' : meeting_list})

def meetingMinutes(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render(request, 'clubapp/meetminutes.html', context=context)

def meetingDetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    return render(request, 'clubapp/meetingdetails.html', {'meet' : meet})

