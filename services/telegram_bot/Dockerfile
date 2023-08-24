FROM python:3.10-slim-bullseye

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install  && poetry install --only settings,telegram_bot,classifier

COPY services/ /app/services/

ENTRYPOINT [ "python", "./services/telegram_bot/main.py" ]
