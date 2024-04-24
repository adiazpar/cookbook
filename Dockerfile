
FROM python:3.11.7-slim

# Key value pair, we named it PYTHONUNBUFFERED:
ENV PYTHONUNBUFFERED=1

# This is the directory that our docker image will work in:
WORKDIR /code

# Copy the requirements.txt file:
COPY requirements.txt .

# Install all the libraries in the requirements.txt file:
RUN pip install -r requirements.txt

COPY . .

# Telling Docker that this is the port that we will be using:
EXPOSE 8000

# This is the default command to run the python server on local host (127.0.0.1)
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
