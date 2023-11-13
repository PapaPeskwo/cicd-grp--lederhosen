FROM python:3.12

WORKDIR /backend

COPY backend/ .
# COPY backend/app.py backend/
# COPY backend/pingurl/ backend/pingurl/
# COPY backend/requirements.txt .

RUN pip install -r requirements.txt

RUN pip install pylint

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
