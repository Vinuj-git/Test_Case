from rest_framework import serializers  
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['name','email','password',]
        # extra_kwargs =  {}

    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        password = validated_data.get('password')
    
        user = User(name=name,email=email)
        user.set_password(password)
        user.save()
        return user
    
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id','author', 'title', 'created_date']
