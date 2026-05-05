# Лабораторная работа 14 — Wikipedia API (FastAPI)

## Описание
REST API для поиска и получения статей из Wikipedia на русском языке.

## Стек
- **Python 3**
- **FastAPI** — веб-фреймворк
- **Pydantic** — валидация данных
- **wikipedia** — обёртка над Wikipedia API

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/article/{title}` | Получить статью по названию |
| `GET` | `/search?query=&limit=` | Поиск статей (limit по умолчанию = 5) |
| `POST` | `/custom-article` | Отправить пользовательскую статью (возвращает как есть) |

## Запуск

```bash
pip install fastapi uvicorn wikipedia pydantic
uvicorn main:app --reload
```

Документация Swagger доступна по адресу: `http://localhost:8000/docs`

## Проделанная работа
- Создано FastAPI-приложение с тремя типами маршрутов (path param, query param, request body)
- Реализована интеграция с Wikipedia API на русском языке
- Настроены Pydantic-схемы для валидации запросов/ответов
- Обработка ошибок (404 при отсутствии статьи, 500 при ошибке поиска)
