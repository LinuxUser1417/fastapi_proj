# FastAPI Blog Application

## Description

This is a simple blog application built with FastAPI, SQLAlchemy, and SQLite for the backend. It features user authentication with hashed passwords and JWTs, post creation, update, delete, and fetch operations. It also includes a rudimentary like and dislike system.

## Setup

1. Ensure that you have Python 3.8 or newer installed on your machine. 

2. Install the necessary Python packages in requirements.txt

or 

///
pip install fastapi uvicorn sqlalchemy pydantic passlib[bcrypt] python-jose[cryptography] python-multipart

3.     Start the FastAPI server by running the following command:

        uvicorn main:app --reload

Testing

You can test the API endpoints using any API client such as Postman or through the automatically generated interactive API documentation provided by FastAPI. To access the documentation, open a web browser and navigate to http://127.0.0.1:8000/docs.

Here, you will find an interactive interface for testing each endpoint. Simply click on an endpoint to expand it, fill in any necessary parameters, and click the "Try it out" button.

4. Commands for Docker:

        sudo docker build -t my-fastapi-app .

        sudo docker run -d -p 8000:8000 my-fastapi-app


----------------------------


**Русский:**

```markdown
# Блог на FastAPI

## Описание

Это простое приложение для блога, созданное с помощью FastAPI, SQLAlchemy и SQLite для бэкенда. Он содержит аутентификацию пользователей с хешированными паролями и JWT, операции создания, обновления, удаления и получения сообщений. Он также включает в себя примитивную систему лайков и дизлайков.

## Настройка

1. Убедитесь, что на вашем компьютере установлен Python 3.8 или новее.

2. Установите необходимые пакеты Python в requirements.txt

или

///
pip install fastapi uvicorn sqlalchemy pydantic passlib[bcrypt] python-jose[cryptography] python-multipart

3.     Запустите сервер FastAPI, выполнив следующую команду:

        uvicorn main:app --reload


Тестирование

Вы можете проверить конечные точки API с помощью любого клиента API, такого как Postman, или через автоматически генерируемую интерактивную документацию API, предоставляемую FastAPI. Чтобы получить доступ к документации, откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000/docs.

Здесь вы найдете интерактивный интерфейс для тестирования каждой конечной точки. Просто нажмите на конечную точку, чтобы раскрыть ее, заполните любые необходимые параметры и нажмите кнопку "Попробовать".

4. Команды для Docker:

        sudo docker build -t my-fastapi-app .
        
        sudo docker run -d -p 8000:8000 my-fastapi-app

