from django.shortcuts import render
# Create your views here.
def sai(request):
    d={'a':300,'b':100}
    return render(request,'sai.html',d)