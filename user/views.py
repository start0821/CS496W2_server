from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
import io

from user.serializer import AccountSerializer
from user.models import Account
from django.db import IntegrityError


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def new(request):
    if(request.method == 'POST'):
        print(request.data)
        try:
            account = Account.objects.get(account__exact=request.data['account'])
            data = AccountSerializer(account, False)
        except Account.DoesNotExist:
            account = Account.objects.create(account=request.data['account'])
            data = AccountSerializer(account, True)
        return Response(data.data, status=status.HTTP_201_CREATED)
