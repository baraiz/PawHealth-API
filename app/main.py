from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import create_db_and_tables, get_session
from app.models import Dog, FeedingLog, WeightEntry, MedicalTreatment

app = FastAPI(
    title="PawHealth API",
    description="Comprehensive health tracking for your dog",
    version="1.1.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- Dog Profile ---
@app.post("/dog", tags=["Profile"], response_model=Dog)
def create_dog(dog: Dog, session: Session = Depends(get_session)):
    session.add(dog)
    session.commit()
    session.refresh(dog)
    return dog

@app.get("/dog", tags=["Profile"], response_model=List[Dog])
def get_dogs(session: Session = Depends(get_session)):
    return session.exec(select(Dog)).all()

# --- Nutrition & Feeding ---
@app.post("/feeding", tags=["Nutrition"], response_model=FeedingLog)
def log_feeding(log: FeedingLog, session: Session = Depends(get_session)):
    session.add(log)
    session.commit()
    session.refresh(log)
    return log

# --- Weight Tracking ---
@app.post("/weight", tags=["Health"], response_model=WeightEntry)
def log_weight(entry: WeightEntry, session: Session = Depends(get_session)):
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry

# --- Medical Records ---
@app.post("/medical", tags=["Health"], response_model=MedicalTreatment)
def log_treatment(treatment: MedicalTreatment, session: Session = Depends(get_session)):
    session.add(treatment)
    session.commit()
    session.refresh(treatment)
    return treatment
