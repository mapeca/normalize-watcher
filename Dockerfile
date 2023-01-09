FROM python:3.10.9-alpine3.17

WORKDIR /usr/src/app

RUN apk add  --no-cache ffmpeg

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir ffmpeg-normalize

COPY ./src .

CMD [ "python", "-u", "./main.py" ]
