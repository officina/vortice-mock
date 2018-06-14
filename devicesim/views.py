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
    if request.method == 'POST':

        obj = json.loads(request.body.decode('utf8'))

        if obj.get("serial") == None:
            return HttpResponse("missing serial", status=400 )

        if obj.get("topic") == None:
            return HttpResponse("missing topic", status=400 )

        if obj.get("certificatePem") == None:
            return HttpResponse("missing certificate", status=400)

    else:
        #chiamo la lambda e registro il certificato
        return method_not_allowed()

    return HttpResponse(status=204)



def hello(request):
    if request.method == 'GET':
        return JsonResponse({
              "model": {
                "version": "3",
                "type": "EVO25"
              },
              "serial": "1234567890",
              "firmware": "1.0.2"
            })
    else:
        return method_not_allowed()

def connect(request):
    if request.method == 'POST':
        # print(str(request.body))
        obj = json.loads(request.body.decode('utf8'))

        if obj.get("__SL_P_P.A") == None:
            return HttpResponse("missing  __SL_P_P.A", status=400 )

        if obj.get("__SL_P_P.C") == None:
            return HttpResponse("missing __SL_P_P.C", status=400)

        if obj.get("__SL_P_N.L") == None:
            return HttpResponse("missing __SL_P_P.C", status=400)

    else:
        #chiamo la lambda e registro il certificato
        return method_not_allowed()

    return HttpResponse(status=204)

def check(request):

    if request.method == 'GET':

        return HttpResponse(status=204)

    else:
        #chiamo la lambda e registro il certificato
        return method_not_allowed()




