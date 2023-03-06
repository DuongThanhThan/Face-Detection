from .models import Face_Detection,Time
from .helper import time_helper

def check_user_exist(user_id):
    check = Face_Detection.objects.filter(user_id = user_id)
    if check:
        return True
    else:
        return False
    

def create_user(user : Face_Detection):
    if check_user_exist(user_id= user.user_id):
        return "User ID already exists"
    else:
        if user.full_name:
            user.created_time = time_helper.now_datetime()
            Face_Detection.objects.create(user_id = user.user_id, full_name = user.full_name, email = user.email, image = user.image, created_time = user.created_time)
            return "User has been successfully initialized"
        else:
            return "Full name cannot be empty"
        
def update_user(user : Face_Detection):

    if user.user_id:
        if check_user_exist(user_id= user.user_id):
            old_user = Face_Detection.objects.get(user_id = user.user_id)

            if user.full_name:
                old_user.full_name = user.full_name
            if user.email:
                old_user.email = user.email
            if user.image:
                old_user.image = user.image
            old_user.save()
            return "Users have been successfully updated"
        else:
            return "User ID does not exist"
    else:
        return "Missing user id"

user = Face_Detection(user_id = 10000, full_name = "Trần Văn B", email = "")

old_user = update_user(user = user)

print(old_user)