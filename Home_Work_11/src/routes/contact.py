from datetime import date, timedelta
from typing import List

from fastapi import Depends, HTTPException, status, Path, APIRouter, Query
from sqlalchemy import or_, and_, extract
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Contact
from src.schemas import ContactResponse, ContactModel
from src.repository import contact as repository_contact

router = APIRouter(prefix="/contacts", tags=['contacts'])


@router.get("/", response_model=List[ContactResponse])
async def get_contact(limit: int = Query(10, le=500), offset: int = 0, db: Session = Depends(get_db)):
    contacts = await repository_contact.get_contact(limit, offset, db)
    return contacts


@router.get("/search")
def search_contacts(query: str, db: Session = Depends(get_db)):
    try:
        contacts = db.query(Contact).filter(
            or_(
                Contact.first_name.ilike(f"%{query}%"),
                Contact.last_name.ilike(f"%{query}%"),
                Contact.email.ilike(f"%{query}%")
            )
        ).all()
        return contacts
    finally:
        db.close()


@router.get("/birthdays", response_model=list[ContactResponse])
def get_upcoming_birthdays(db: Session = Depends(get_db)):
    try:
        today = date.today()
        end_date = today + timedelta(days=7)
        contacts = db.query(Contact).filter(
            and_(
                extract('month', Contact.birthday) == today.month,
                extract('day', Contact.birthday) >= today.day,
                extract('day', Contact.birthday) <= end_date.day
            )
        ).all()
        return contacts
    finally:
        db.close()


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contact.get_contact_by_id(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contact.create(body, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contact.update(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contact.remove(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


