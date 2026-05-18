# Hotels

Веб-сервис для поиска отелей и бронирований.

## Стек

- FastAPI
- PostgreSQL + SQLAlchemy (async) + Alembic
- Redis (кеш `fastapi-cache`, брокер Celery)
- Celery (фоновые задачи, обработка изображений)
- SQLAdmin (админ-панель)
- Jinja2 templates (страницы в `templates/`)
- Docker

## Требования

- Python 3.11+
- PostgreSQL 14+
- Redis 6+
- Docker

## Переменные окружения

Настройки читаются из `.env`. Пример содержимого файла `.env` можно найти в файле `.env.example`.

## Установка зависимостей

Для установки всех необходимых зависимостей, используйте файл `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Быстрый старт с Docker

1.  **Соберите Docker-образ:**

    ```bash
    docker build -t hotels-app .
    ```

2.  **Запустите контейнер с приложением:**

    Не забудьте передать необходимые переменные окружения. Вы можете сделать это, создав файл `.env` на основе `.env.example` и передав его с помощью флага `--env-file`.

    ```bash
    docker run -p 8000:8000 --env-file .env hotels-app
    ```

3.  **Откройте:**

    *   Swagger UI: `http://127.0.0.1:8000/docs`
    *   Admin (SQLAdmin): `http://127.0.0.1:8000/admin`

## Быстрый старт (без Docker)

1. Поднимите PostgreSQL и Redis.

Пример через Docker:

```bash
docker run --name hotels-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
docker run --name hotels-redis -p 6379:6379 -d redis:7
```

2. Создайте и активируйте виртуальное окружение, установите зависимости.

```bash
pip install -r requirements.txt
```

3. Примените миграции:

```bash
alembic upgrade head
```

4. Запустите API:

```bash
uvicorn main:app --reload
```

Откройте:

- Swagger UI: `http://127.0.0.1:8000/docs`
- Admin (SQLAdmin): `http://127.0.0.1:8000/admin`

## Фоновые задачи (Celery)

Для обработки изображений из эндпоинта `POST /images/hotels` поднимите worker:

```bash
celery -A tasks.celery.celery worker -l info
```

## Основные эндпоинты

- `GET /` проверка, что сервис жив
- `GET /hotels` пример поиска (параметры: `location`, `date_from`, `date_to`, опционально `has_spa`, `stars`)
- `POST /auth/register` регистрация
- `POST /auth/login` логин (ставит cookie `booking_access_token`)
- `GET /bookings` список бронирований текущего пользователя
- `POST /bookings` создание бронирования (query: `room_id`, `date_from`, `date_to`)
- `POST /images/hotels` загрузка картинки отеля + постановка задачи Celery на ресайз
- `GET /pages/hotels` HTML-страница (шаблон `templates/hotels.html`)

## Тесты

```bash
pytest
```

## Тестовые данные

В корне есть `test_data_db.sql` (можно загрузить в PostgreSQL через `psql -f test_data_db.sql`).
