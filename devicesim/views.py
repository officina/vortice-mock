from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
import json
import os
from mockserver.settings import PROJECT_ROOT


# Create your views here.
def method_not_allowed():

    return HttpResponseNotAllowed("<h4>Method not allowed</h4>")

def register(request):
    if request.method == 'GET':

        return HttpResponse("Method <b>Get</b> not allowed")

    elif request.method == 'POST':

        obj = json.loads(request.body.decode('utf8'))

        if obj.get("serial") == None:
            return HttpResponse("missing serial", status=400 )

        if obj.get("topic") == None:
            return HttpResponse("missing topic", status=400 )

        if obj.get("certificate") == None:
            return HttpResponse("missing certifica ", status=400)


        #chiamo la lambda e registro il certificato

        return HttpResponse(status=200)



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

def check(request):

    if request.method == 'GET':

        return HttpResponse(status=200)

    if request.method == 'POST':

        return HttpResponse("Method <b>Get</b> not allowed")




