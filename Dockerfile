FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic passlib[bcrypt] python-jose[cryptography] python-multipart

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
