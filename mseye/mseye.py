from flask import Flask
import requests
from PIL import Image
from io import BytesIO
import hashlib
import binascii
import os

mseye = Flask(__name__)

DATA_DIR='/home/pmatos/Projects/ms-eye/data'

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
    return path
