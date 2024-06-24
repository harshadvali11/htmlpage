from django.shortcuts import render

# Create your views here.

def kasak(request):
    return render(request,'kasak.html')

def kirak(request):
    return render(request,'kirak.html')