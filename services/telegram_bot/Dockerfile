FROM python:3.10.11

WORKDIR /app

RUN apt-get -y update; apt-get -y install curl
RUN mkdir -p services/classifier/models/
RUN curl -o services/classifier/models/1.0 https://classifier-models.sfo3.digitaloceanspaces.com/1.0.pickle

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install  && poetry install --only settings,bot,classifier

RUN sudo apt-get install nvidia-cuda-toolkit nvidia-cuda-toolkit-gcc

COPY services/ /app/services/
COPY services/telegram_bot/main.py /app/main.py

ENTRYPOINT [ "python", "main.py" ]
