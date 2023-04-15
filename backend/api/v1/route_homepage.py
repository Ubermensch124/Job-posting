from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
homepage_router = APIRouter()


@homepage_router.get("/homepage")
async def homepage(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})
