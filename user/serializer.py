from user.models import Account
from rest_framework import serializers
from django.db import IntegrityError
import io
import json
from rest_framework.parsers import JSONParser


class AccountSerializer(Account):

    def __init__(self,object,isFirst):
        self.data = {'account':object.account, 'pk':object.pk, 'is_first':isFirst}

    class Meta:
        pass
