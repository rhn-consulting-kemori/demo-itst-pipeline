FROM python:3.13.2

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

# ENV Parameter
# DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

CMD ["python", "app.py"]
