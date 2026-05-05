# Лабораторная работа 14 - Wikipedia API (FastAPI)

## Описание
REST API сервис для поиска и получения статей из Wikipedia с использованием FastAPI.

## Технологии
- **Python 3**
- **FastAPI** - веб-фреймворк
- **Pydantic** - валидация данных
- **wikipedia** - обертка над Wikipedia API

## API Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/article/{title}` | Получение статьи по названию |
| `GET` | `/search?query=&limit=` | Поиск статей (limit по умолчанию = 5) |
| `POST` | `/custom-article` | Создание пользовательской статьи (с валидацией через Pydantic) |

## Выполненная работа
- Реализован FastAPI-сервис с тремя типами эндпоинтов (path param, query param, request body)
- Интеграция с Wikipedia API для поиска и получения статей
- Использование Pydantic-моделей для валидации входящих/исходящих данных
- Обработка ошибок API (404 при отсутствии статьи, 500 при ошибке API)

## Как запустить
```bash
pip install fastapi uvicorn wikipedia pydantic
uvicorn main:app --reload
```

Swagger документация будет доступна по адресу: `http://localhost:8000/docs`

## Документация
PDF с описанием лабораторной работы: `Лабораторная работа №14.pdf`
