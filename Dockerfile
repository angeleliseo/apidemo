FROM tiangolo/uvicorn-gunicorn-fastapi
COPY ./app /app
RUN pip install -r requirements.txt
