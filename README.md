# FastAPI + PostgreSQL App

REST API на FastAPI с PostgreSQL в Docker Compose.

## Технологии

- Python 3.11
- FastAPI
- PostgreSQL 15
- SQLAlchemy
- Docker Compose

## Требования

- Docker
- Docker Compose

## Быстрый старт

Клонируй репозиторий:

```bash
git clone https://github.com/tiltimmy/fastapi-postgres-app.git
cd fastapi-postgres-app
```

Создай файл `.env`:

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret123
POSTGRES_DB=mydb
DATABASE_URL=postgresql://admin:secret123@db:5432/mydb
```

Запусти:

```bash
docker compose up --build
```

## Эндпоинты

API будет доступен на `http://localhost:8000`

Документация Swagger: `http://localhost:8000/docs`

- `GET /` — проверка что API работает
- `GET /health` — health check
- `POST /sites?url=...` — добавить сайт
- `GET /sites` — получить список всех сайтов

## Архитектура

Два контейнера:
- `api` — FastAPI приложение
- `db` — PostgreSQL база данных

Данные базы сохраняются в Docker volume между перезапусками.
