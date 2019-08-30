from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import divers
from djreservation.views import ProductReservationView
def index(request):
    
    diverslist = divers.objects.all()
    context ={
        'names': diverslist
    }
    return render(request ,'divers/index.html',context)

def id(request,id):
    diver = divers.objects.all()
    for x in diver:
        if x.id == id:
            context = {
                'name': x
            }
            return render(request ,'divers/diverprofile.html',context)
    
def search(request,searchq):
    diverslist = divers.objects.all()
    filterddivers = []
    for x in diverslist:
        if x.location == searchq:
            filterddivers.append(x)
    context = {
        'names': filterddivers
        }
        
    return render(request ,'divers/searchreport.html',context)
# Create your views here.


