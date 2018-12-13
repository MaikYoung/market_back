import fp as fp
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import serializers
from django.core import serializers as django_serializer
from rest_framework.response import Response
from rest_framework.utils import json

from admins.models import Admin
from stores.models import Store


class AdminSerializer(serializers.ModelSerializer):
    stores_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Admin
        fields = ('pk', 'email', 'first_name', 'last_name', 'username', 'phone', 'stores_by_user')

    def get_stores_by_user(self, obj):
        objects = Store.objects.filter(manager=obj.pk)
        if len(objects) > 0:
            return objects.values()
