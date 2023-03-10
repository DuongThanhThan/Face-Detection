import os
import cv2
import numpy as np
import _face_detection as ftk
import re
# import sys
import os

class FaceDetection:
    verification_threshold = 0.8
    detection_model, recognition_model = None, None
    image_size = 160
    def __init__(self):
        FaceDetection.load_models() 

    @staticmethod
    def get_dir_current():
        dir_current = os.path.dirname(os.path.abspath(__file__))
        return dir_current

    @staticmethod
    def load_models():
        if not FaceDetection.detection_model: #Face Detection model run fisrt
            print("This is dir_path",FaceDetection.get_dir_current())
            FaceDetection.detection_model = FaceDetection.load_face_detection()

        if not FaceDetection.recognition_model: #Face Recognition model run after
            FaceDetection.recognition_model = FaceDetection.load_face_recognition()
        
    @staticmethod
    def load_face_recognition():
        model_path = FaceDetection.get_dir_current() + "/Models/OpenCV/opencv_face_detector_uint8.pb"
        model_pbtxt = FaceDetection.get_dir_current() + "/Models/OpenCV/opencv_face_detector.pbtxt"
        net = cv2.dnn.readNetFromTensorflow(model_path, model_pbtxt)
        return net

    @staticmethod
    def load_face_detection():
        v = ftk.Verification()
        v.load_model(FaceDetection.get_dir_current()+"/Models/FaceDetection/")
        v.initial_input_output_tensors()
        return v

    @staticmethod
    def compare(emb1, emb2):
        diff1 = np.subtract(emb1, emb2)
        diff = np.sum(np.square(diff1))
        error = diff / np.sum(np.square(emb1))
        return diff < FaceDetection.verification_threshold, diff, error

    @staticmethod
    def detect_faces(image): 
        height, width, channels = image.shape
        blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), [104, 117, 123], False, False)
        FaceDetection.recognition_model.setInput(blob)
        detections = FaceDetection.recognition_model.forward()
        faces = []

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                x1 = int(detections[0, 0, i, 3] * width)
                y1 = int(detections[0, 0, i, 4] * height)
                x2 = int(detections[0, 0, i, 5] * width)
                y2 = int(detections[0, 0, i, 6] * height)
                faces.append([x1, y1, x2 - x1, y2 - y1])
        return faces

    @staticmethod
    def load_face_embeddings(image_dir):
        embeddings = {}
        for file in os.listdir(image_dir):
            img_path = image_dir + file
            try:
                image = cv2.imread(img_path)
                faces = FaceDetection.detect_faces(image)
                if len(faces) == 1:
                    x, y, w, h = faces[0]
                    image = image[y:y + h, x:x + w]
                    embeddings[file.split(".")[0]] = FaceDetection.detection_model.img_to_encoding(cv2.resize(image, (160, 160)), FaceDetection.image_size)
                else:
                    print(f"Found more than 1 face in \"{file}\", skipping embeddings for the image.")
            except Exception:
                print(f"Unable to read file: {file}")
        return embeddings

    @staticmethod
    def fetch_detections(image, embeddings):
        faces = FaceDetection.detect_faces(image)
        detections = []
        for face in faces:
            x, y, w, h = face
            im_face = image[y:y + h, x:x + w]
            img = cv2.resize(im_face, (200, 200))
            user_embed = FaceDetection.detection_model.img_to_encoding(cv2.resize(img, (160, 160)), FaceDetection.image_size)
            
            detected = {}
            detected2 = []
            for _user in embeddings:
                flag, thresh, err = FaceDetection.compare(embeddings[_user], user_embed)
                # print("Error",_user, err )
                detected2.append(err)
                if flag:
                    detected[_user] = thresh
            
            detected = {k: v for k, v in sorted(detected.items(), key=lambda item: item[1])}
            detected = list(detected.keys())
            if len(detected) > 0:
                detections.append(detected[0])
        return detections, detected2

def face_recognition(image_or_video_path=None,face_dir=FaceDetection.get_dir_current()+"/faces/"):
    FaceDetection.load_models()
    embeddings = FaceDetection.load_face_embeddings(face_dir)
    waitkey_variable = 1
    image_flip = False
    if image_or_video_path:
        print("Using path: ", image_or_video_path)
        cap = cv2.VideoCapture(image_or_video_path)
        if int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) == 1:
            waitkey_variable = 0
    else:
        print("Capturing from webcam")
        image_flip = True
        cap = cv2.VideoCapture(0)
    while 1:
        ret, image = cap.read()
        if image_flip:
	        image = cv2.flip(image, 1)
        if not ret:
            return
        detected_person, err_array = FaceDetection.fetch_detections(image, embeddings)
        people = list(embeddings.keys())
        detected_person_min = err_array.index(min(err_array))
        detected_person = re.findall("^[A-Za-z\s]*", people[detected_person_min])[0]
        key = cv2.waitKey(waitkey_variable)
        if key & 0xFF == ord("q"):
            break
        return detected_person
