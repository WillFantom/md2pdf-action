ARG PYTHON_VERSION=3.10
ARG ALPINE_VERSION=3.15
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

RUN apk add --no-cache --virtual .build-deps \
  gcc \
  jpeg-dev \
  libffi-dev \
  musl-dev \ 
  zlib-dev && \
  apk add --no-cache \
  cairo-dev \
  font-noto-emoji \
  terminus-font ttf-inconsolata ttf-dejavu font-noto ttf-font-awesome font-noto-extra \
  gdk-pixbuf-dev \ 
  pango-dev  && \
  pip install markdown2 pygments weasyprint && \
  apk del .build-deps

RUN wget https://github.com/google/fonts/archive/main.tar.gz -O google-fonts.tar.gz && \
  tar -xf google-fonts.tar.gz && \
  rm -f google-fonts.tar.gz && \
  mkdir -p /usr/share/fonts/truetype/google-fonts && \
  find $PWD/fonts-main/ -name "*.ttf" -exec install -m644 {} /usr/share/fonts/truetype/google-fonts/ \;  && \
  fc-cache -f && rm -rf /var/cache/*

COPY entrypoint.py /app/entrypoint.py

ENTRYPOINT [ "python3", "/app/entrypoint.py" ]
