FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /cooperChallenge
WORKDIR /cooperChallenge
COPY . /cooperChallenge/
RUN pip install -r requirements.txt