FROM alpine:3.9.5

RUN apk update && apk add \
    python3 \
    py3-flask \
    && pip3 install youtube_dl

COPY ./app /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
