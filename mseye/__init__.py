from flask import Flask, render_template, url_for
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
SERVER_ADDR='192.168.178.56'

me.connect('mseye')


@mseye.route('/')
def showall():
    snaps = EyeSnap.objects().order_by('timestamp')

    recent = snaps[0]
    old = snaps[1:]

    return render_template('showall.html',
                           vipsnap=recent,
                           others=old)


@mseye.route('/sight-beyond-sight')
def get_current_image():
    rep = requests.get('http://{}/jpg/image.jpg'.format(SERVER_ADDR),
                           auth=('pmatos', 'iamIr0nman'))
    print(rep.status_code)
    print(rep.encoding)

    stream = BytesIO(rep.content)
    image = Image.open(stream)
    checksum = hashlib.sha256(stream.getvalue()).digest()
    filename = '.'.join([binascii.hexlify(checksum).decode('utf-8'), 'jpg'])
    path = os.path.join(DATA_DIR, filename)
    image.save(path)

    esnap = EyeSnap(datetime.now(), path)
    esnap.save()

    return render_template('sight.html', snap=esnap)
