from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json

from .serializer import ContactSerializer
from django.core import serializers as seri
from .models import Contact
from user.models import Account
# Create your views here.
@csrf_exempt
@api_view(['PUT','GET','DELETE'])
@parser_classes((JSONParser,))
def detail(request,pk):


    if request.method == 'GET':
        contact = Contact.objects.filter(account__pk=pk)
        serializers = ContactSerializer(contact,many=True)
        return JsonResponse(serializers.data, safe=False)


    elif request.method == 'PUT':
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return HttpResponse(status=404)
        print(request.data,456)
        print('put', request.data)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return HttpResponse(status=404)
        contact.delete()
        print('delete')
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['POST','GET'])
def index(request):
    if request.method == 'POST':
        contact = Contact.objects.create(account = Account.objects.get(pk=request.data['id']),
                                         name = request.data['name'],
                                         phone_number = request.data['phone_number'])
        # serializer = ContactSerializer(data=request.data)
        print("adfasdfasdf")
        # contact = Contact(serializer)
        # print("--------------------------------------------")
        # contact.account = Account.objects.get(pk=request.data['id'])
        # if contact.is_valid():
        contact.save()
        print(contact)
        return JsonResponse(contact.as_json())
        # return Response(contact.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        contacts = Contact.objects.all()
        serializers = ContactSerializer(contacts,many=True)
        return JsonResponse(serializers.data, safe=False)
