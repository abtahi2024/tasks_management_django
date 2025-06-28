from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>welcome home</h1>")

def show_task(request):
    return HttpResponse('This is our task')

def abtahi(a):
    return HttpResponse("<h1 style='color: red'>Abtahi</h1>")

def show_specific_task(request,id):
    return HttpResponse("This is specific task")

def show_admin(request):
    return HttpResponse("This is admin")