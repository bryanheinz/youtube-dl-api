FROM alpine:3.9.5

RUN apk update && apk add \
    python3 \
    py3-flask \
    && wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl \
    && chmod a+rx /usr/local/bin/youtube-dl

COPY ./app /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
