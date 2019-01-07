# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Your imports
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from . serializers import employeeSerializer

# Create your views here.
class employeeList(APIView):

  def get(self, request):
    objects = employee.objects.all()
    serializer=employeeSerializer(objects, many=True)
    return Response(serializer.data)

  def post(self):
    pass
