from django.http import response
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')
