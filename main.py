from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wikipedia

# Инициализация FastAPI и настройка Wikipedia
app = FastAPI()
wikipedia.set_lang("ru")  # Устанавливаем язык (русский)

# Схемы Pydantic
class ArticleResponse(BaseModel):
    title: str
    content: str

class SearchResponse(BaseModel):
    results: list[dict]

class ArticleRequest(BaseModel):
    title: str
    content: str

# Роут с параметром пути (path parameter)
@app.get("/article/{title}", response_model=ArticleResponse)
def get_article(title: str):
    """Получить статью по её названию"""
    try:
        page = wikipedia.page(title)
        return {"title": page.title, "content": page.content}
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Статья не найдена")

# Роут с параметром запроса (query parameter)
@app.get("/search", response_model=SearchResponse)
def search_articles(query: str, limit: int = 5):
    """Поиск статей по запросу"""
    results = wikipedia.search(query, results=limit)
    formatted_results = [{"title": title, "summary": wikipedia.summary(title)} for title in results]
    return {"results": formatted_results}

# Роут с телом запроса (POST + body)
@app.post("/custom-article", response_model=ArticleRequest)
def create_custom_article(article: ArticleRequest):
    """Добавить пользовательскую статью (пример работы с телом запроса)"""
    # Здесь можно добавить логику сохранения статьи в базу данных
    return article