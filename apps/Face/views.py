from .models import Face_Detection,Time
from .helper import time_helper, image_helper
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from .seializers import CreateUserValidator, UpdateUserValidator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import simplejson as json
from PIL import Image
import numpy as np
import face_recognition
import cv2

import numpy as np
import cv2
import face_recognition
import simplejson as json



class CGUD_User(ViewSet):
    @action('POST', True)
    def create(self, request: Request):
        try:
            data = request.data
            data_serializer = CreateUserValidator(data=data)

            if not data_serializer.is_valid():
                return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            image_user = request.data.get("image").read()
            nparr = np.frombuffer(image_user, np.uint8)

            # Sau này thay vào bằng cách biến đổi vector 128 chiều của Phát
            img = cv2.imdecode(nparr, 1)
            img_enc = face_recognition.face_encodings(img)[0]
            #---------------------------------------------

            created_time = time_helper.now_datetime()
<<<<<<< HEAD:apps/Face/views.py
=======
            user = Face_Detection(**data_serializer.validated_data)

            user.image = str(img_enc.tolist())


            user.created_time = created_time

            user.save()
>>>>>>> 6680004 (new version):Face/views.py

            image_user = data.get("image").read()
            nparr = np.frombuffer(image_user, np.uint8)
            img = cv2.imdecode(nparr, 1)
            print(face_recognition.face_encodings(img))
            img_enc = face_recognition.face_encodings(img)[0]
            img_str = str(img_enc.tolist())


            main_data = {
                "user_id" : data.get("user_id"),
                "full_name" : data.get("full_name"),
                "email" : data.get("email"),
                "created_time" : created_time
            }

            Face_Detection.objects.create(**main_data, image = img_str)
            response_data = {
                'message': 'Success',
                'data':main_data
            }

            return Response(response_data)
        
        except Exception as e:
            response_data = {
                'message': 'Error',
                'data':str(e)
            }
            return Response(response_data)
        
    @action('GET', True)
    def get_user(self, request:Request):
        try:
            data = request.data
            user_id = data.get("user_id")
            if (not user_id) or (not Face_Detection.objects.filter(user_id = user_id).count()):
                response_data = {
                    'message':'Error',
                    'data':"not exist"
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            
        
            user = Face_Detection.objects.get(user_id = user_id)
            
            main_data = {
                "user_id":data.get("user_id"),
                "full_name":user.full_name,
                "email":user.email,
                "created_time":user.created_time
            }

            image = user.image

            #List image
            list_image_128 = image_helper.list_image(str(image))

            response_data = {
                'message':'Success',
                'data':main_data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'message': 'Error',
                'data': str(e)
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
            
            if (not user_id) or (not Face_Detection.objects.filter(user_id = user_id).count()):
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
        


class User(ViewSet):
    @action('get', True)
    def get(self, request: Request):
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

            json_data = {
                "user_id": user.user_id,
                "full_name": user.full_name,
                "email": user.email,
                "image": image_helper.list_image(str(user.image)),
                "created_time": user.created_time

            }


            response_data = {
                'message':'Success',
                'data': json_data
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {
                'message': 'Error',
                'data': str(e)
            }
            return Response(response_data)

