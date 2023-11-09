FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP app:create_app

# Expose port 5000 (default Flask port)
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
