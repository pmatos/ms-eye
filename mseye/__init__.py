from flask import Flask
from flask_script import Manager
import mongoengine as me
import requests
from PIL import Image
from io import BytesIO
from eyesnap import EyeSnap
from datetime import datetime
import hashlib
import binascii
import os

mseye = Flask(__name__)
manager = Manager(mseye)

DATA_DIR=os.path.join(mseye.root_path, 'data')

me.connect('mseye')


@mseye.route('/')
def hello_world():
    return 'Hello, World!'


@mseye.route('/sight-beyond-sight')
def get_current_image():
    r = requests.get('http://192.168.178.56/jpg/image.jpg', auth=('pmatos', 'iamIr0nman'))
    print(r.status_code)
    print(r.encoding)

    stream = BytesIO(r.content)
    image = Image.open(stream)
    checksum = hashlib.sha256(stream.getvalue()).digest()
    filename = '.'.join([binascii.hexlify(checksum).decode('utf-8'), 'jpg'])
    path = os.path.join(DATA_DIR, filename)
    image.save(path)

    es = EyeSnap(datetime.now(), path)
    es.save()

    return render_template('sight.html', eyeimg=url_for('static', 'eye.jpg'), snap=es)
