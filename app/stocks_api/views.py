from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    """
    view for home page
    """
    return render(request, 'stocks_api/index.html')

def about(request):
    """ view for about page"""
    return HttpResponse("hello about page")

def getapi(request):
    """view to registring page"""
    return HttpResponse("get your api")

def api(request):
    return JsonResponse({'hello': 'api'})