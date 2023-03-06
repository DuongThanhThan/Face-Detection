from .serializer import Face_Serializers
from .models import Face_Detection,Time

def check_user_exist(user_id):
    check = Face_Detection.objects.filter(user_id = user_id)

    if check:
        return True
    else:
        return False

def create_user(user : Face_Detection):
    face_user = Face_Serializers(data = user)
    if face_user.is_valid():
        print("OK")
    else:
        print("NOT OK")

user = Face_Detection(user_id = 10000, full_name = "Nguyen Van A")

create_user(user)