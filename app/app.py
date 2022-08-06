#!/usr/bin/env python3

import youdl
import config
from flask import Flask, request, abort, Response


__version__ = '1.1.0'

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
    try:
        use_ytdl = request.args.get('ytdl')
        content = request.json
    except Exception as e:
        print(e, flush=True)
        abort(Response(f"Error processing request.", 500))
    
    try:
        url = content['url']
    except KeyError:
        abort(Response(
            "please include a video URL for the key 'url'.", status=400))
    
    try:
        if use_ytdl:
            youdl.dl(url)
        else:
            youdl.ytdlp(url)
    except Exception as e:
        print(e, flush=True)
        abort(Response("internal server error", status=500))
    
    return Response(
        {'response':'downloading video'}, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
