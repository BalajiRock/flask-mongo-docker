FROM python

WORKDIR /app

COPY . /app

RUN pip install Flask pymongo

EXPOSE 5000

ENV FLASK_APP=app.py

# Run flask app
CMD ["flask", "run", "--host=0.0.0.0"]
