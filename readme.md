# youtube-dl-api
This project is a small Python Flask API server to take video URLs and download the video using youtube-dl.

## Getting started
The easiest way to get setup and running is to use Docker.

- Clone this repo
- Copy config-sample to config.py
- Edit config.py
  - Fill in an API and Flask key (easy mode: generate UUIDs for the keys)
  - Fill in a download path (leave alone if using Docker)
- Edit docker-compose.yml
  - Edit the port if you'd like to change it
  - Edit the video path if you'd like to change it
- Run `docker-compose --build` to build the image
- Run `docker-compose up -d` to run it

Sending requests to the API server:

```shell
curl -X "POST" "http://0.0.0.0:5000/youtube-dl" \
     -H 'api_key: API_KEY' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{"url": "https://www.youtube.com/watch?v=3QtklTXbKUQ"}'
```
