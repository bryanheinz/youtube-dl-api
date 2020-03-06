#!/usr/bin/env python3
import os
import youtubes
import app_config
import base64 as b64
from flask import Flask, render_template, redirect, request, jsonify, abort, Response


config = app_config.get_config()

if config:
    api_key = config['api_key']
    flask_key = config = ['flask_key']


app = Flask(__name__)
app.secret_key = flask_key
api_key = api_key


# check for API key in the headers
def checkAppKey(fn):
    def inner(*args, **kwargs):
        try:
            key = request.headers.get('apikey')
            if key != api_key:
                raise(abort(
                    Response("access denied", status=401)
                ))
        except KeyError:
            raise(abort(
                Response("invalid request", status=400)
            ))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    return inner


@app.route('/')
@checkAppKey
def hello_world():
    return(Response(status=200))

@app.route('/youtube-dl', methods=['GET', 'POST'])
@checkAppKey
def youtube_dl():
    content = request.json
    try:
        url = content['url']
    except KeyError:
        raise(abort(Response(
            "please enclude a base64 encoded URL for the key 'url'",
            status=400
        )))
    
    try:
        url = b64.b64decode(url)
    except Exception as e:
        print(e)
        raise(abort(Response(
            "please base64 encode your url",
            status=400
        )))
    
    try:
        youtubes.dl(url)
    except Exception as e:
        print(e)
        raise(abort(Response(
            "internal server error",
            status=500
        )))
    
    return(Response(status=200))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
