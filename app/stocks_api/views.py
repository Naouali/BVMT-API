from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

@api_view (['GET'])
def api(request):
    return Response({'hello': 'api'})