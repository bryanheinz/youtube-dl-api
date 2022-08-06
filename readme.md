# youtube-dl-api
This project is a small Python Flask API server to take video URLs and download the video using [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [youtube-dl](https://github.com/ytdl-org/youtube-dl/).

## Getting started

The easiest way to get setup and running is to use Docker.

- Clone this repo
- Duplicate configs/config-sample.py to app/config.py
- Edit app/config.py
  - Fill in an API and Flask key (easy mode: generate UUIDs for the keys)
  - Leave everything else alone if using Docker
- Duplicate the yt-dlp-sample.conf as yt-dlp.conf if you want to [supply your own config](https://github.com/yt-dlp/yt-dlp#configuration)
- Duplicate docker-compose-sample.yml as docker-compose.yml
  - Edit the port if you'd like to change it
  - Edit the downloads source path if you'd like to change it
  - Uncomment and edit the yt-dlp config source if you want to supply your own config
- Run `docker-compose --build` to build the image
- Run `docker-compose up -d` to run it

Sending requests to the API server:

```shell
curl -X "POST" "http://localhost:5000/youtube-dl" \
     -H 'api_key: API_KEY' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{"url": "https://www.youtube.com/watch?v=3QtklTXbKUQ"}'
```
