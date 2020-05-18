from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    view for home page
    """
    return render(request, 'stocks_api/index.html')

def about(request):
    """ view for about page"""
    return HttpResponse("hello about page")