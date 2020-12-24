import os
import hashlib
from flask import (Flask, request, redirect, url_for, send_from_directory,
                   render_template)
from werkzeug import secure_filename
from datetime import datetime
from hashlib import sha256

UPLOAD_FOLDER = './files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
INS = None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html')

'''
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

            owner = request.form["owner"]
            filehash = sha256(path).hexdigest()
            filesize = os.path.getsize(path)

            return redirect(url_for('uploaded_file',
                                    filename=filename,
                                    filehash=filehash))
    return render_template("upload.html")


@app.route('/uploader')
def uploaded_file():
    filename = request.args['filename']
    filehash = request.args['filehash']
    return render_template("uploaded.html",
                           filename=filename,
                           filehash=filehash)


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/info/<filehash>')
def get_file_info(filehash):
    file_info = contract.get_file_info(INS, filehash)
    info = {
        "file_name": file_info[0],
        "upload_date": datetime.fromtimestamp(file_info[1]),
        "file_size": file_info[2],
    }
    return render_template("info.html",
                           filehash=filehash,
                           info=info)


@app.route('/check', methods=['POST'])
def check_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        filehash = sha256(path).hexdigest()
        return render_template('check.html',
                               is_exist=True,
                               filehash=filehash,
                               filename=filename)
'''

if __name__ == "__main__":
    app.run(debug=False)
