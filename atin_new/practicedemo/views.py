from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from practicedemo.models import *

# Create your views here.



class SelectionMember(APIView):
    def post(self,request,*args,**kwargs):
        total_data=request.data
        first_name=total_data.get("first_name")
        last_name=total_data.get("last_name")
        age=total_data.get("age")
        data_create=Member.objects.create(**total_data)
        return Response({"msg":"successfully created","status":200})


