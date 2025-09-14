from flask import Flask, request, send_from_directory, render_template, abort, redirect, url_for, flash, jsonify
from itsdangerous import URLSafeTimedSerializer
import os
import mimetypes
from datetime import datetime
app = Flask(__name__)
app.secret_key="BharathTube3675858###636&9"
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5* 1024 * 1024 * 1024  # GB limit for files , change first value if you want

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        try:
            file.save(file_path)
            return jsonify({"message": "File uploaded successfully!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route('/')
def index():
    filenames = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("home.html", filenames=filenames)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/stream/<filename>')
def stream_video(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        abort(404)

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = "video/mp4"  
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash("File deleted successfully!", "warning")
        return redirect(url_for('index'))
    else:
        abort(404)
import socket, qrcode, io
from flask import send_file

def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip



@app.route('/qr/<filename>')
def generate_qr(filename):
    file_name=filename
    host_ip = get_host_ip()
    link = f"http://{host_ip}:5000/download/{file_name}"

    qr = qrcode.make(link)
    buf = io.BytesIO()
    qr.save(buf, 'PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)
