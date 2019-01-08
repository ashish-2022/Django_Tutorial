from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

# Create your views here.
class appStatus(APIView):
  renderer_classes = (JSONRenderer, )

  def get(self, request):
    strJson = {'status':'OK'}
    return Response(strJson)

