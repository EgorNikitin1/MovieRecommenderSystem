from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ml.model import movies, similarity, recommend

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/similar", response_class=HTMLResponse)
async def search(request: Request, movie_name: str):
    recommend_list = recommend(movie_name)

    return templates.TemplateResponse("index.html", {"request": request, "results": recommend_list})