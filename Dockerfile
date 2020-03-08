FROM alpine:3.9.5

RUN apk update && apk add \
    ffmpeg \
    python3 \
    py3-flask \
    py3-gunicorn \
    && wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl \
    && chmod a+rx /usr/local/bin/youtube-dl

# COPY ./app /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:5000", "app:app"]
