from .models import Face_Detection,Time
from .helper import time_helper
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from .seializers import CreateUserValidator, UpdateUserValidator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action




class CUD_User(ViewSet):

    @action('POST', True)
    def create(self, request: Request):
        try:
            data = request.data
            data_serializer = CreateUserValidator(data=data)

            if not data_serializer.is_valid():
                return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            created_time = time_helper.now_datetime()
            Face_Detection.objects.create(**data_serializer.validated_data, created_time = created_time)

            response_data = {
                'message': 'Success',
                'data': data_serializer.validated_data
            }        
            return Response(response_data)
        except Exception as e:
            response_data = {
                'message': 'Error',
                'data':str(e)
            }
            return Response(response_data)
        

    @action('PATCH', True)
    def update(self, request: Request):
        try:
            data = request.data
            data_serializer = UpdateUserValidator(data=data)

            if not data_serializer.is_valid():
                return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            data_serializer = data_serializer.validated_data

            old_data = Face_Detection.objects.get(user_id = data_serializer.get("user_id"))
            print(old_data)

            old_data.email = old_data.email if old_data.email else data_serializer.get("email")
            old_data.full_name = old_data.full_name if old_data.full_name else data_serializer.get("full_name")
            old_data.image = old_data.image if old_data.image else data_serializer.get("image")

            old_data.save()

            response_data = {
                'message': 'Success',
                'data': data_serializer
            }        
            return Response(response_data)

        except Exception as e:
            response_data = {
                'message': 'Error',
                'data': str(e)
            }
            return Response(response_data)
        
    @action('delete', True)
    def delete(self, request: Request):
        try:
            data = request.data

            user_id = data.get("user_id")
            


            if not user_id:
                response_data = {
                    'message':'Error',
                    'data':"not exist"
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            
            user = Face_Detection.objects.get(user_id = user_id)

            user.delete()
            response_data = {
                'message':'Success',
                'data':'Mất tiêu luôn'
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {
                'message': 'Error',
                'data': str(e)
            }
            return Response(response_data)

