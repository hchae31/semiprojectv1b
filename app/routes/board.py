from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from starlette.templating import Jinja2Templates
board_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')

@board_router.get('/list', response_class=HTMLResponse)
async def list(req: Request):
    return templates.TemplateResponse('board/list.html', {'request': req})

@board_router.get('/write', response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('board/write.html', {'request': req})

@board_router.get('/view', response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('member/view.html', {'request': req})