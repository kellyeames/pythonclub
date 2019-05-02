from django.shortcuts import render
from .models import Resource

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html' ,{'resource_list' : resource_list})