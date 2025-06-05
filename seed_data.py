from datetime import datetime, timedelta
from database import SessionLocal
from models_db import FitnessClass
from utils import ist_to_utc

def seed():
    db = SessionLocal()
    if db.query(FitnessClass).first():
        return

    classes = [
        FitnessClass(
            name="Yoga",
            datetime=ist_to_utc(datetime.now() + timedelta(days=1, hours=8)),
            instructor="Anita",
            slots=5
        ),
        FitnessClass(
            name="Zumba",
            datetime=ist_to_utc(datetime.now() + timedelta(days=2, hours=18)),
            instructor="Rahul",
            slots=8
        ),
        FitnessClass(
            name="HIIT",
            datetime=ist_to_utc(datetime.now() + timedelta(days=3, hours=7)),
            instructor="Sneha",
            slots=10
        ),
    ]

    db.add_all(classes)
    db.commit()
    db.close()
