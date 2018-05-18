from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
import json



# Create your views here.
def method_not_allowed():

    return HttpResponseNotAllowed("<h4>Method not allowed</h4>")

def register(request):
    if request.method == 'GET':

        return HttpResponse("Method <b>Get</b> not allowed")

    elif request.method == 'POST':

        return JsonResponse({'serial': 'i8s689sd8f98sdfksdfkhsdf6'})



def hello(request):
    return JsonResponse({'serial': 'i8s689sd8f98sdfksdfkhsdf6'})

def connect(request):
    if request.method == 'GET':

        return HttpResponse("Method <b>Get</b> not allowed")

    elif request.method == 'POST':
        print(str(request.body))
        obj = json.loads(request.body.decode('utf8'))

        if obj.get("ssid") == None:
            return HttpResponse("missing  SSID", status=400 )

        if obj.get("password") == None:
            return HttpResponse("missing password ", status=400)

        return HttpResponse(status=204)


