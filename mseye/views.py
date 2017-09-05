import binascii
import os
import hashlib
from datetime import datetime
from io import BytesIO
import mongoengine as me
import requests
from PIL import Image
from mseye import app
from mseye.eyesnap import EyeSnap
from flask import render_template, send_from_directory


SERVER_ADDR = '192.168.178.56'

me.connect('mseye')


@app.route('/')
def showall():
    snaps_qs = EyeSnap.objects().order_by('timestamp')

    return render_template('showall.html',
                           qs=snaps_qs)


@app.route('/sight-beyond-sight')
def get_current_image():
    rep = requests.get('http://{}/jpg/image.jpg'.format(SERVER_ADDR),
                       auth=('pmatos', 'iamIr0nman'))
    print(rep.status_code)
    print(rep.encoding)

    stream = BytesIO(rep.content)
    image = Image.open(stream)
    checksum = hashlib.sha256(stream.getvalue()).digest()
    filename = '.'.join([binascii.hexlify(checksum).decode('utf-8'), 'jpg'])
    path = os.path.join(app.config['DATA'], filename)
    image.save(path)

    esnap = EyeSnap(datetime.now(), filename)
    esnap.save()

    return render_template('sight.html',
                           snap=esnap)


@app.route('/data/<filename>')
def send_file(filename):
    return send_from_directory(app.config['DATA'], filename)
