from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import engine, Base, SessionLocal
import models  # pydantic schemas
import models_db  # ORM models - ensure imported for metadata
import crud
import seed_data
import utils

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# seed initial data
seed_data.seed()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/classes", response_model=List[models.ClassOut])
def list_classes(tz: str = Query("Asia/Kolkata"), db: Session = Depends(get_db)):
    classes = crud.get_all_classes(db)
    for cls in classes:
        cls.datetime = utils.utc_to_timezone(cls.datetime, tz)
        cls.available_slots = cls.slots
    return classes

@app.post("/book", response_model=models.BookingOut)
def book_class(booking: models.BookingRequest, db: Session = Depends(get_db)):
    result = crud.create_booking(db, booking)
    if not result:
        raise HTTPException(status_code=400, detail="Class full or not found")
    return result

@app.get("/bookings", response_model=List[models.BookingOut])
def get_bookings(email: str, db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)
