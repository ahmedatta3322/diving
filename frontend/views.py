from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    return render(request, "frontend/index.html")
def register(request):
    return render(request, "frontend/register.html")
