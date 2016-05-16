import os

from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Neruda"
    tpl_name = 'index.html'

    return render_template(tpl_name, library_name=library_name)