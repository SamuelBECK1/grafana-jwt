FROM python:3.11.3-bullseye
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask jwcrypto pyjwt
COPY . /srv
ENV FLASK_APP=app
CMD ["python","app.py"]
