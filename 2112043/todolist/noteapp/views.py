from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def balikpapan(request):
    return render(request,'balikpapan.html')