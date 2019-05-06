FROM python:2.7.14-slim

# https://stackoverflow.com/a/46407052/2107339
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    build-essential

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt

# move relevant files
ADD app.py .
ADD todos_store.py .
ADD static/ ./static

#ENV FLASK_APP "app.py"
CMD ["python", "app.py"]




