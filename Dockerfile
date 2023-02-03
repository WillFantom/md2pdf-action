ARG PYTHON_VERSION=3.11
ARG ALPINE_VERSION=3.17
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

RUN apk add --no-cache --virtual .build-deps \
  gcc \
  jpeg-dev \
  libffi-dev \
  musl-dev \ 
  zlib-dev && \
  apk add --no-cache \
  cairo-dev \
  font-noto-all font-noto-emoji \
  gdk-pixbuf-dev \ 
  pango-dev  && \
  pip install markdown2 pygments weasyprint

RUN apk del .build-deps && \
  fc-cache -fv && \
  rm -rf /var/cache/*

COPY entrypoint.py /app/entrypoint.py

ENTRYPOINT [ "python3", "/app/entrypoint.py" ]
