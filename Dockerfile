FROM alpine:3.16

RUN apk add --no-cache \
    ffmpeg \
    python3 \
    py3-flask \
    py3-gunicorn

COPY ./app /app
COPY ./configs/yt-dlp-sample.conf /root/yt-dlp.conf
COPY ./startup.sh /startup.sh

WORKDIR /app

EXPOSE 5000

CMD ["/startup.sh"]
