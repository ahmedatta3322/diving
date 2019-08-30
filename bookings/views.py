from django.shortcuts import render
from .forms import divebook
from django.http import HttpResponse
from divers.models import divers
# Create your views here.
def index(request,pk,location):
    if request.method == 'POST':
        f = divebook(request.POST)
        return HttpResponse(f)
    else :
        diver = divers.objects.all()
        f = divebook(initial={'diver': diver.get(pk=pk) ,'location': location , 'cost': diver.get(pk=pk).gcost })
    return render(request,'bookings/index.html',{'f':f})
  
