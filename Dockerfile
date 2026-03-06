FROM python:3.13-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY package.json ./
RUN npm install

COPY . .

RUN npm run build:css

RUN chmod 755 /code/start-django.sh

EXPOSE 8000

ENTRYPOINT ["/code/start-django.sh"]