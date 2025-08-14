from flask import Flask, render_template, request, jsonify
from utils.face_utils import load_known_faces, process_uploaded_image
import face_recognition

app = Flask(__name__)

known_encodings, known_names = load_known_faces()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    file = request.files['image']
    unknown_encoding = process_uploaded_image(file)

    if unknown_encoding is None:
        return jsonify({'result': 'No face detected.'})

    matches = face_recognition.compare_faces(known_encodings, unknown_encoding)
    if True in matches:
        matched_index = matches.index(True)
        return jsonify({'result': 'Match found: ' + known_names[matched_index]})
    else:
        return jsonify({'result': 'No match found.'})

if __name__ == '__main__':
    app.run(debug=True)