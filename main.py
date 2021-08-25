from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import schemas, models
# from inspection import inspection


app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name='static')

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def create(request: Request, db: Session = Depends(get_db)):
    stats = db.query(models.Stats.id, models.Stats.body).all()
    return templates.TemplateResponse("stats.html",{"request":request,"ng_num":stats[2][1]})


@app.get("/save")
async def save():
    pass
    

@app.get("/save/get")
async def root():
    pass


@app.get("/save/visualization")
async def root():
    pass


@app.get("/infer")
async def root(request: Request):
    # 검사 for loop
    # inspection(True, request.query_params['isBlue'], request.query_params['isBack'])

    return RedirectResponse("/infer/visualization", 303)

    # return RedirectResponse(f"/infer/get?{request.query_params}", 303)


@app.get("/infer/visualization", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("infer.html",{"request":request})





@app.get("/display-result")
async def root():
    pass


@app.get("/display-result/inspection-{iter}")
async def root():
    pass


@app.get("/display-result/inspection-{iter}/patch-{idx}")
async def root():
    pass


@app.get("/display-result/infer-exp")
async def root():
    pass