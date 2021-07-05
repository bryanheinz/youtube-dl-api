#!/usr/bin/env python3
import os
import youdl
import config
import base64 as b64
from flask import Flask, render_template, redirect, request, jsonify, abort, Response


api_key = config.api_key
flask_key = config.flask_key


app = Flask(__name__)
app.secret_key = flask_key


# check for API key in the headers
def checkAppKey(fn):
    def inner(*args, **kwargs):
        try:
            key = request.headers.get('api_key')
            if key != api_key:
                abort(Response("access denied", status=401))
        except KeyError:
            abort(Response("invalid request", status=400))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    return inner


@app.route('/')
@checkAppKey
def hello_world():
    return Response(status=200)

@app.route('/youtube-dl', methods=['GET', 'POST'])
@checkAppKey
def youtube_dl():
    content = request.json
    try:
        url = content['url']
    except KeyError:
        abort(Response(
            "please include a video URL for the key 'url'.", status=400))
    
    try:
        youdl.dl(url)
    except Exception as e:
        print(e, flush=True)
        abort(Response("internal server error", status=500))
    
    return Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
