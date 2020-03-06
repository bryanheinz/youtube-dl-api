# youtube-dl-api
Small Python Flask API server to take video URLs and download them with youtube-dl.

On first run, it will generate a config file, `ydl.conf`. Save this file and pass it into Docker to keep using the same API key `-v ./ydl.conf:/app/ydl.conf`.

