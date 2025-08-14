import face_recognition
import cv2
import numpy as np
import os

def load_known_faces(path='static/known_faces/', target_size=(150, 150)):
    known_encodings = []
    known_names = []

    for filename in os.listdir(path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = face_recognition.load_image_file(os.path.join(path, filename))
            face_locations = face_recognition.face_locations(image)

            if not face_locations:
                continue

            top, right, bottom, left = face_locations[0]
            face_image = image[top:bottom, left:right]
            face_image = cv2.resize(face_image, target_size)

            encodings = face_recognition.face_encodings(face_image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(filename.split('.')[0])

    return known_encodings, known_names

def process_uploaded_image(file, target_size=(150, 150)):
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_img)
    if not face_locations:
        return None

    top, right, bottom, left = face_locations[0]
    face_image = rgb_img[top:bottom, left:right]
    face_image = cv2.resize(face_image, target_size)

    encodings = face_recognition.face_encodings(face_image)
    if encodings:
        return encodings[0]
    else:
        return None