from typing import List
from datetime import datetime
from fastapi import APIRouter, Request, UploadFile, File, Form, Depends
import os
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
from app.schema.gallery import NewGallery
gallery_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')



@gallery_router.get('/list/{cpg}', response_class=HTMLResponse)
async def list(req: Request, cpg: int, db: Session = Depends(get_db)):
    try:
        return templates.TemplateResponse('/gallery/list.html',
                                          {'request': req })

    except Exception as ex:
        print(f'▷▷▷ list 오류 발생 : {str(ex)}')
        return RedirectResponse(url='/gallery/error', status_code=303)

@gallery_router.get('/write', response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('gallery/write.html', {'request': req})

@gallery_router.post('/write', response_class=HTMLResponse)
async def write(req: Request, title: str = Form(...), userid: str = Form(...),
                contents: str = Form(...), files: List[UploadFile] = File()):
    print(title, userid, contents)
    print(files)

    UPLOAD_PATH = 'C:/Java/nginx-1.26.2/html/cdn/img'
    attachs = [] # 업로드된 파일정보를 저장하기 위해 리스트 생성
    today = datetime.today().strftime('%Y%m%d%H%M%S') # UID 생성
    for file in files:
        if file.filename != '' and file.size > 0:
            nfname = f'{today}{file.filename}'
            # os.path.join(A, B) => A/B (경로생성)
            fname = os.path.join(UPLOAD_PATH, file.filename) # 업로드할 파일경로
            content = await file.read() #업로드할 파일의 내용을 비동기로 읽음
            with open(fname, 'wb') as f:
                f.write(content)
            attach = [nfname, file.size]  # 업로드된 파일 정보 리스트에 저장
            attachs.append(attach)

    print(attachs)

    return templates.TemplateResponse('gallery/write.html', {'request': req})

@gallery_router.get('/view', response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('gallery/view.html', {'request': req})