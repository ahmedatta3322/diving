from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    return render(request, "frontend/index.html")
def register(request):
    return render(request, "frontend/register.html")
def create(request):
    return render(request, "frontend/create.html")
def view(request):
    return render(request, "frontend/view.html")