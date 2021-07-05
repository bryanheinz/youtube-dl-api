#!/bin/sh
wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl
gunicorn -w 4 -b 0.0.0.0:5000 app:app
