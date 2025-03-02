
FROM python:3.9


WORKDIR /app


COPY ./app/requirements.txt ./requirements.txt


RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


COPY ./app /app


CMD ["fastapi", "run", "main.py", "--port", "8000"]