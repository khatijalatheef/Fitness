from sqlalchemy.orm import Session
from datetime import datetime
import models_db
import models


def get_all_classes(db: Session):
    return db.query(models_db.FitnessClass).filter(models_db.FitnessClass.datetime >= datetime.utcnow()).all()

def get_class_by_id(db: Session, class_id: int):
    return db.query(models_db.FitnessClass).filter(models_db.FitnessClass.id == class_id).first()

def create_booking(db: Session, booking: models.BookingRequest):
    fitness_class = get_class_by_id(db, booking.class_id)
    if fitness_class and fitness_class.slots > 0:
        fitness_class.slots -= 1
        db_booking = models_db.Booking(**booking.dict())
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    return None

def get_bookings_by_email(db: Session, email: str):
    return db.query(models_db.Booking).filter(models_db.Booking.client_email == email).all()
