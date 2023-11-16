FROM python:3.12

WORKDIR /backend

COPY .pylintrc /backend

COPY backend/ .

RUN pip install -r requirements.txt

RUN pip install pylint

RUN pip install pytest

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g newman

RUN pylint .

EXPOSE 5000

ENV PYTHONPATH /backend
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
