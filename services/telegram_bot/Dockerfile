FROM python:3.10-slim-bullseye

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install  && poetry install --only settings,telegram_bot,classifier

RUN curl -o services/classifier/models/1.0 https://classifier-models.sfo3.digitaloceanspaces.com/1.0.pickle

COPY services/ /app/services/

ENTRYPOINT [ "python", "./services/telegram_bot/main.py" ]