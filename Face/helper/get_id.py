import sys
sys.path.insert(1, '../Face_Model')
import face_recognition_main as Face

def get_id(img_path) :
    user_id = Face.face_recognition(img_path)
    return user_id


if __name__ == '__main__':
    print(get_id("../../Face/Face_Model/input/TheRock.jpeg"))