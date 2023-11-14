FROM python:3.12

WORKDIR /backend

COPY .pylintrc /testbackend

COPY backendtest/ .

RUN pip install -r requirements.txtfaf

RUN pip install pylint

RUN pylint .

EXPOSE 5000

ENV PYTHONPATH /backend
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
