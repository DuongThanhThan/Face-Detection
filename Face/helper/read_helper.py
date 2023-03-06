from app import settings
from app.db import Connect_Collection
from . import time_helper
from app.messages import FACE_STATUS, DEVICE

import cv2
import face_recognition
import numpy as np

collect_face = Connect_Collection().connect_collect_Face()
collect_user_check = Connect_Collection().connect_collect_UserCheck()
collect_device = Connect_Collection().connect_collect_Device()

def read_video(bytes_string):
    with open(settings.PATH_FILE_STATIC_VIDEO, 'wb') as wfile:
        wfile.write(bytes_string)
    wfile.close()
        
def read_img(path):
    img = cv2.imread(path)
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)

    height = int(h * ratio)
    return cv2.resize(img, (width, height))

def authen(name_device, img_enc , count_frame , max_frame):
    response = {
        'name' : FACE_STATUS["ERROR"],
        'id' : FACE_STATUS["ERROR"],
        'device' : name_device,
    }



    # tìm tất cả các document trong collection Face
    for doc in collect_face.find():           
        known_encode = np.asmatrix(doc.get("image_encode")) 

        # So sánh encode của frame với các encode trong document từ database   
        result = face_recognition.compare_faces(known_encode, img_enc,tolerance = 0.4)

       # Nếu có bất kỳ giá trị nào là True trong danh sách result thì lấy ra tên của người ở document đấy 
        for res in result:
            if res == True:
                response = {
                    'name' : doc.get("username"),
                    'id' : doc.get("id_name"),
                    'device' : name_device
                }
                response["created"] = time_helper.now_datetime()

                # thêm vào database user_check lịch sử authen
                collect_user_check.insert_one(response)

                # chuyển count_frame bằng -1 để nhận biết là đã authen
                count_frame = -1
                return count_frame

    # Nếu sau 3 lần authen mà vẫn không tìm ra người nào thì name là unknown         
    if count_frame / max_frame == 3:
        response["created"] = time_helper.now_datetime()
        collect_user_check.insert_one(response)
        count_frame = -1
        return count_frame

    # Tăng count frame thêm 1 đơn vị
    count_frame = count_frame + 1

    return count_frame