from flask import Flask, request, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image part', 400
    image = request.files['image']
    if image.filename == '':
        return 'No selected file', 400
    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)
    return 'Upload successful', 200

@app.route('/gallery')
def gallery():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('gallery.html', images=files)

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/gallery-json')
def gallery_json():
    files = os.listdir(UPLOAD_FOLDER)
    urls = [f"https://flask-gallery-server.onrender.com/static/uploads/{file}" for file in files]
    return jsonify(urls)
@app.route('/gallery-json')
def gallery_json():
    files = os.listdir(UPLOAD_FOLDER)
    urls = [f"https://flask-gallery-server.onrender.com/static/uploads/{file}" for file in files]
    return jsonify(urls)

if __name__ == '__main__':
    app.run()
