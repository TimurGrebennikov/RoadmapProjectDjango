# Hotel Booking API

API сервис для управления номерами отеля и бронированиями.

## Технологии

- Python 3.12
- Django 6.0
- Django REST Framework
- PostgreSQL
- Docker
- Loguru (логирование)
- Ruff, Mypy, Bandit, Radon (качество кода)
- Pre-commit hooks

## Быстрый запуск

### 1. Клонировать репозиторий


git clone <url-репозитория>
cd RoadmapProjectDjango
1. Запустить через Docker
bash
docker-compose up --build
Миграции применяются автоматически при запуске.

2. API доступно по адресу
text
http://localhost:8000/api/v1/
API Эндпоинты
Номера (Rooms)
Метод	URL	Описание
GET	/api/v1/rooms/	Список всех номеров
POST	/api/v1/rooms/create/	Создать номер
DELETE	/api/v1/rooms/delete/<id>/	Удалить номер
Брони (Bookings)
Метод	URL	Описание
GET	/api/v1/bookings/list/?room_id=<id>	Список броней номера
POST	/api/v1/bookings/create/	Создать бронь
DELETE	/api/v1/bookings/delete/<id>/	Удалить бронь
Примеры запросов
Создать номер
bash
curl -X POST http://localhost:8000/api/v1/rooms/create/ \
  -d "description=Люкс" \
  -d "price=15000"
Ответ:

json
{"id":1,"description":"Люкс","price":"15000.00","created_at":"2026-05-31T18:30:00Z"}
Получить список номеров
bash
curl http://localhost:8000/api/v1/rooms/
Ответ:


[{"id":1,"description":"Люкс","price":"15000.00","created_at":"2026-05-31T18:30:00Z"}]
Создать бронь
bash
curl -X POST http://localhost:8000/api/v1/bookings/create/ \
  -d "room_id=1" \
  -d "start_date=2025-01-10" \
  -d "end_date=2025-01-15"
Ответ:

json
{"id":1,"room":1,"start_date":"2025-01-10","end_date":"2025-01-15","date_of_creation":"2026-05-31"}
Получить список броней номера
bash
curl "http://localhost:8000/api/v1/bookings/list/?room_id=1"
Ответ:

json
[{"id":1,"room":1,"start_date":"2025-01-10","end_date":"2025-01-15","date_of_creation":"2026-05-31"}]
Удалить бронь
bash
curl -X DELETE http://localhost:8000/api/v1/bookings/delete/1/
Удалить номер
bash
curl -X DELETE http://localhost:8000/api/v1/rooms/delete/1/
Логирование
Логи настроены через Loguru:

Dev режим (APP_ENV=dev): цветные логи в консоль

Prod режим (APP_ENV=prod): JSON-логи для систем сбора

Файловые логи: ротация 10 MB, хранение 7 дней, архивация zip

Просмотр логов:

bash
docker logs -f django_app
Запуск тестов
bash
docker exec -it django_app python manage.py test
Остановка
bash
docker-compose down
Переменные окружения
Переменная	По умолчанию	Описание
APP_ENV	dev	Режим работы (dev/prod)
LOG_LEVEL	INFO	Уровень логирования
DB_NAME	hotel_db	Имя БД
DB_USER	postgres	Пользователь БД
DB_PASSWORD	mysecretpassword	Пароль БД
DB_HOST	db	Хост БД
DB_PORT	5432	Порт БД
Структура проекта
text
src/
├── api/v1/payment/
│   ├── views.py          # API эндпоинты
│   ├── serializers.py    # Сериализаторы DRF
│   └── urls.py           # Маршруты
├── apps/payment/
│   ├── models.py         # Модели Rooms, Bookings
│   └── tests.py          # Тесты
├── config/
│   ├── settings.py       # Настройки Django
│   ├── urls.py           # Главные маршруты
│   └── logging_setup.py  # Настройка Loguru
└── manage.py
