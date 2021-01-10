import os
import hashlib
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
from datetime import datetime
from flask_cors import CORS
import json
'''
from celery import Celery
import ipfshttpclient
'''
import web3_test
import hashlib import sha256
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


@app.rooute('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
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

@app.route('/crypto')
def encrypt():
    a = request.args.get('', '')
    task = encrypt_task.delay(a)
    task_result = task.get()
    return 

@celery.task
def encrypt_task(data):
    from base64 import b64encode
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import add
    from Crypto.Random import get_random_bytes
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.jdumps({'iv':iv, 'ciphertext':ct})
    return result

@celery.task
def decrypt_task(data):
    from base64 import b64decode
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    
    json_input = data
    try:
        b64 = json.loads(json_input)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])

        cipher = AES.new(key, AES.MODE_CBC, iv)
        print(f"size of block = {AES.block_size}")
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)
    except ValueError:
        print("Incorrect decryption")
    except KeyError:
        print("Incorrect decryption")

@celery.task
def upload_on_blockchain():
    pass

def sha256_checksum(filename, block_size=65536):
    pass

if __name__ == "__main__":
    # INS = contract.deploy()
    app.run(host='0.0.0.0')
