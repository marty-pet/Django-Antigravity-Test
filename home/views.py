from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Sveiki atvykę į Marty Django projektą su Antigravity AI!')
