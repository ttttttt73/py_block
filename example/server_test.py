import os
import hashlib
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
from datetime import datetime
from flask_cors import CORS
'''
from celery import Celery
import ipfshttpclient
'''
import web3_test

'''
api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

app.config.update(
    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
celery = make_celery(app)
CORS(app)
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
            filehash = sha256_checksum(path)
            filesize = os.path.getsize(path)
            upload_on_blockchain(filehash=filehash, filename=filename, filesize=filesize, owner=owner)
            return redirect(url_for('uploaded_file', filename=filename, filehash=filehash))
    return render_template("uploaded.html")


@app.route('/uploader')
def uploaded_file():
    filename = request.args['filename']
    filehash = request.args['filehash']
    return render_template("uploaded.html", filename=filename, filehash=filehash)

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/info/<filehash>')
def get_file_info(filehash):
    file_info = contract.get_file_info(INS, filehash)
    info = {
        "file_name": file_info[0],
        "upload_data": datetime.fromtimestamp(file_info[1]),
        "file_size": file_info[2],
        }
    return render_template("info.html", filehash=filehash, info=info)

@app.route('/check', methods=['POST'])
def check_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        filehash = sha256_checksum(path)
        is_exist = contract.check_file_exist(INS, filehash)
        return render_template('check.html', is_exist=is_exist, filehash=filehash, filename=filename)

@celery.task
def upload_on_blockchain():
    pass


def sha256_checksum(filename, block_size=65536):
    pass


if __name__ == "__main__":
    INS = contract.deploy()
    app.run(host='0.0.0.0')
