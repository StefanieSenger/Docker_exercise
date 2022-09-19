ARG PYTHON_VERSION=3.8.12
FROM python:$PYTHON_VERSION
WORKDIR /app
COPY . .
ENTRYPOINT [ "python", "stupid_coach.py" ]
