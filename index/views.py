from django.shortcuts import render
from divers import views
from .forms import Searchform , Datesearch
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import redirect
# Create your views here.
def index(request):
    if request.method == 'POST':
        locationform = Searchform(request.POST)
        if locationform.is_valid():
            cd = locationform.cleaned_data["searchname"]
            return redirect(f'/divers/{cd}')
    else:
        locationform = Searchform()
    return render(request,'index.html',{'form': locationform})



    