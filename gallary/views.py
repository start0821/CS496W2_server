from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json
from user.models import Account
from .models import Image
from io import BytesIO
# Create your views here.
@csrf_exempt
@api_view(['POST','GET'])
def index(request):
    if request.method == 'POST':
        try:
            user = Account.objects.get(pk=request.data['Id'])
        except Account.DoesNotExist:
            print("not found")
            return JsonResponse(json.dumps({'errer':request.data[id]+'인 계정을 찾을 수 없습니다.'}),status=HttpHTTP_204_NO_CONTENT)
        image = Image(file=request.data['file'],owner=user)
        image.save()
        files = list()
        try:
            files.append(open(settings.BASE_DIR + image.file.url,'rb').read())
        except:
            return JsonResponse(json.dumps({'errer':'이미지 에러'}),status=HTTP_204_NO_CONTENT)
        response = FileResponse(streaming_content=files)
        response['Content-Type'] = 'image/png'
        response['boundary'] = '3131623adb2043caaeb5538cc7aa0b3a'
        return response

    elif request.method == 'GET':
        images = [Image.objects.get(pk=1),Image.objects.get(pk=2)]
        files = list()
        for image in images:
            files.append(open(settings.BASE_DIR + image.file.url,'rb').read())
        response = FileResponse(streaming_content=files)
        response['Content-Type'] = 'multipart/form-data'
        response['boundary'] = '3131623adb2043caaeb5538cc7aa0b3a'
        print(response)
        return response

@csrf_exempt
@api_view(['PUT','GET'])
@parser_classes((JSONParser,))
def detail(request,pk):

    if request.method == 'GET':
        try:
            user = Account.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return HttpResponse(status=404)
        images = Image.objects.filter(user__pk=user.id)
        # for
# TODO: 여러 파일을 어떻게 보낼지 생각해보기.
        return Response(serializer.data)

    elif request.method == 'PUT':
        print(request.data,456)
        print('put', request.data)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        contact.delete()
        print('delete')
        return HttpResponse(status=204)
