from dataclasses import field
from itertools import product
from pyexpat import model
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
