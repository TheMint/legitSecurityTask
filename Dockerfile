FROM python:3.11-slim

ENV POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN apt-get update && apt-get install -y curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="$POETRY_HOME/bin:$PATH" && \
    poetry --version

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /src

COPY pyproject.toml poetry.lock /src/
COPY src /src/

RUN poetry install --no-root

RUN apt-get update && apt-get install -y nodejs npm && \
    npm install -g smee-client && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 3000

CMD ["./run.sh"]
