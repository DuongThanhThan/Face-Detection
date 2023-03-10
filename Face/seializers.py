from rest_framework import serializers
from django.db.models import Q
from .models import Face_Detection
import re


class CreateUserValidator(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    full_name = serializers.CharField(max_length=255, required=True)
<<<<<<< HEAD:Face/seializers.py
=======
    # image = serializers.CharField(required = True)
>>>>>>> 2257d60 (image upload):apps/Face/seializers.py
    email = serializers.EmailField()


    class Meta:
        model = Face_Detection
        fields = ['user_id',
              'full_name',
              'email',]
        
    def validate(self, data):
        if data['user_id']:
            user_id_exist_check = Face_Detection.objects.filter(Q(user_id=data['user_id'])).count()
            if user_id_exist_check:
                raise serializers.ValidationError("User already existed")
            return data
        
class UpdateUserValidator(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    full_name = serializers.CharField(max_length=255)
    image = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Face_Detection

    def validate(self, data):
        if data['user_id']:
            user_id_exist_check = Face_Detection.objects.filter(Q(user_id=data['user_id'])).count()         
            if not user_id_exist_check:
                raise serializers.ValidationError("User does not exist")
            return data
        
    