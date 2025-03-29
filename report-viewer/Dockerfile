FROM python:3.13.2

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

# ENV Parameter
ENV DB_USER=postgres
ENV DB_PASS=postgres
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432
ENV DB_NAME=postgres

EXPOSE 8088

CMD ["python", "app.py"]
