FROM python:3.8-slim

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt

# move relevant files
ADD app.py .
ADD todos_store.py .
ADD static/ ./static

#ENV FLASK_APP "app.py"
CMD ["python", "app.py"]




