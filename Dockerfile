FROM python

WORKDIR /app

COPY . /app

RUN pip install Flask pymongo flask_bcrypt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
