FROM python:3.12

WORKDIR /backend

COPY .pylintrc /backend

COPY backend/ .

COPY ./newman_tests ./newman_tests

RUN pip install -r requirements.txt

RUN pip install pylint

RUN pip install pytest

RUN apt-get update && apt-get install -y nodejs npm

RUN npm install -g newman

RUN pylint .

EXPOSE 5000

ENV PYTHONPATH /backend
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
