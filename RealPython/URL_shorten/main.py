import secrets
from requests import Session
import validators
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
import models, schemas, crud
from database import SessionLocal, engine

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)

app = FastAPI()

@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    db_url = crud.create_db_url(db=db, url=url)
    db_url.url = db_url.key
    db_url.admin_url = db_url.secret_key

    return db_url

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


@app.get("/{url_key}")
def forward_to_target_url(
    url_key:str, 
    request: Request,
    db: Session = Depends(get_db)
    ):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)


@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"