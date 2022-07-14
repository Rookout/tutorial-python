FROM python:3.8-slim

# pip installing the requirements.txt requires git because we're installing a fork
RUN apt-get -y update
RUN apt-get -y install git wget

ARG GIT_COMMIT=unspecified
ENV ROOKOUT_COMMIT=$GIT_COMMIT

ARG GIT_ORIGIN=unspecified
ENV ROOKOUT_REMOTE_ORIGIN=$GIT_ORIGIN

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt

# move relevant files
ADD app.py .
ADD todos_store.py .
COPY utils/ ./utils
ADD static/ ./static

#ENV FLASK_APP "app.py"
CMD ["python", "app.py"]




