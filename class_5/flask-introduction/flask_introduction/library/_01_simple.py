import os

from flask import Flask, make_response, g


app = Flask(__name__)


def check_user_auth():
    print("Checking user")


@app.before_request
def before_request():
    check_user_auth()
    # read user from db
    g.user = {
        'id': 99,
        'name': 'John'
    }


@app.route('/')
def hello_world():
    resp = make_response("Hello world. Welcome {}".format(g.user['name']))
    resp.status_code = 201
    return resp


@app.route('/g2')
def g2():
    #check_user_auth()
    return "We're G2"
    
@app.route('/g3')
def g3():
    #check_user_auth()
    return "We're G2"

