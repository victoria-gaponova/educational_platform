FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir educational_platform

WORKDIR educational_platform

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh