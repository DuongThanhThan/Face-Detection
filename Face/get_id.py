import sys
sys.path.insert(1, '../Face_Model')
import face_recognition_main as Face

print(Face.face_recognition("input/TheRock.jpeg"))
