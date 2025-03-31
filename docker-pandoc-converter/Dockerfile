FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and fonts
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc wget curl gnupg unzip git \
    python3 python3-pip \
    texlive-xetex texlive-fonts-recommended texlive-plain-generic \
    fonts-lmodern fonts-dejavu fonts-freefont-ttf \
    wkhtmltopdf poppler-utils libreoffice \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
RUN pip3 install --upgrade pip && pip3 install \
    flask \
    pandocfilters \
    pygments \
    panflute \
    markdown2

COPY /pandoc /app
WORKDIR /app

ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
