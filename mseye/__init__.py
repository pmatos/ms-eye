import os
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
app.config['DATA'] = os.path.join(app.root_path, 'data')
Manager(app)

import mseye.views
