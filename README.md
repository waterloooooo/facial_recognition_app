# 🧠 Facial Recognition Web App

A simple facial recognition web application built with Flask and [face_recognition](https://github.com/ageitgey/face_recognition). Users can upload images via a browser, and the app will identify any faces it recognizes based on a known database.

---

## 📸 Features

- Upload an image through a web interface
- Detect and recognize faces in the image
- Compare against pre-saved known faces
- JSON response with the match result

---

## 🧱 Tech Stack

- **Flask** – Web framework
- **face_recognition** – Facial recognition powered by dlib
- **OpenCV (cv2)** – Image decoding and preprocessing
- **NumPy** – Image buffer handling
- **HTML/CSS** – Basic front-end via Jinja2

---

## 📁 Folder Structure

```

facial\_recognition\_app/
├── app.py
├── requirements.txt
├── static/
│   ├── known\_faces/     # Images of known people (e.g., alice.jpg)
│   └── uploads/         # Temporary uploaded images
├── templates/
│   └── index.html       # Upload form
├── utils/
│   └── face\_utils.py    # Facial recognition logic

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/waterloooooo/facial_recognition_app.git
cd facial_recognition_app
````

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Known Faces

Place images of known people inside the `static/known_faces/` directory.

* **Example**: `alice.jpg`, `bob.png`
* The filename (without extension) will be used as the person’s name.

### 5. Run the App

```bash
python app.py
```

Open your browser and navigate to:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🔍 How It Works

* Upload a photo via the form on the homepage.
* The app:

  1. Extracts the first face from the uploaded image.
  2. Encodes it and compares it against all known faces.
  3. Returns the matching name or "No match found."

---

## 🧪 Example

If `static/known_faces/` contains:

```
alice.jpg
bob.jpg
```

And you upload a photo of Alice →
📤 The app will return:

```json
{ "result": "Match found: alice" }
```

---

## 📦 Deployment Notes

This app is lightweight and can be deployed on:

* Heroku (with buildpacks for dlib)
* Render.com
* Docker
* PythonAnywhere (with OpenCV support)