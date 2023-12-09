from fastapi import FastAPI, Request, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import models
from sqlalchemy.orm import Session
from database import engine, get_db
import datetime
from fastapi.responses import RedirectResponse


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

template = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


@app.post("/add")
def add(
    request: Request,
    db: Session = Depends(get_db),
    email: str = Form(...),
    name: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    created_date=datetime.datetime.utcnow(),
):
    new_user = models.User(
        email=email,
        name=name,
        message_subject=subject,
        message=message,
        created_at=created_date,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return template.TemplateResponse(
        "index.html", {"request": request,"messages": "Thanks for your feedback"}
    )



@app.get("/admin")
async def admin(request: Request, db: Session = Depends(get_db)):
    get_data = db.query(models.User).all()
    return template.TemplateResponse(
        "admin.html", {"request": {"url": str(request.url)}, "data": get_data}
    )
