from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Dog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1)  # Name cannot be empty
    breed: str = Field(min_length=2) # Breed must have at least 2 characters
    chip_number: Optional[str] = None

class WeightEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    weight_kg: float = Field(gt=0)  # Weight must be greater than 0
    date: datetime = Field(default_factory=datetime.now)

class FeedingLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount_grams: int = Field(gt=0) # Amount must be positive
    food_type: str = Field(min_length=2)
    timestamp: datetime = Field(default_factory=datetime.now)

class MedicalTreatment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=2)
    type: str
    date: datetime
    next_due_date: Optional[datetime] = None
