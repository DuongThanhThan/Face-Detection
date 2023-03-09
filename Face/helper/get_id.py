import sys
sys.path.insert(1, '../Face_Model')
import face_recognition_main as Face

def get_id(img_path) :
    user_id = Face.face_recognition(img_path)
    return user_id

if __name__ == '__main__':
    import os
    parent = parent = os.path.join(os.getcwd(), os.pardir)
    parent_path = os.path.abspath(parent)
    print(get_id(parent_path+"/Face_Model/input/test.mp4"))