from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contact(limit: int, offset: int, db: Session):
    """
    The get_contact function returns a list of contacts from the database.
        Args:
            limit (int): The number of contacts to return.
            offset (int): The starting point for the query.

    :param limit: int: Limit the number of contacts returned
    :param offset: int: Determine the offset of the query
    :param db: Session: Pass the database session to the function
    :return: A list of contacts
    :doc-author: Trelent
    """
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    """
    The get_contact_by_id function returns a contact object from the database based on its id.
        Args:
            contact_id (int): The id of the desired contact.
            db (Session): A connection to the database.

    :param contact_id: int: Specify the id of the contact we want to retrieve
    :param db: Session: Pass the database session to the function
    :return: The contact with the specified id
    :doc-author: Trelent
    """
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def create(body: ContactModel, db: Session):
    """
    The create function creates a new contact in the database.
        It takes a ContactModel object as input and returns the newly created contact.

    :param body: ContactModel: Get the data from the request body
    :param db: Session: Access the database
    :return: A contact object
    :doc-author: Trelent
    """
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update(contact_id: int, body: ContactModel, db: Session):
    """
    The update function takes in a contact_id, body, and db.
    It then gets the contact by id from the database. If it exists,
    it updates all of its fields with those provided in the body.

    :param contact_id: int: Get the contact by id
    :param body: ContactModel: Pass the data from the request body to be used in creating a new contact
    :param db: Session: Pass the database session to the function
    :return: The updated contact object
    :doc-author: Trelent
    """
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.additional_data = body.additional_data
        db.commit()
    return contact


async def remove(contact_id: int, db: Session):
    """
    The remove function removes a contact from the database.
        Args:
            contact_id (int): The id of the contact to be removed.
            db (Session): A connection to the database.

    :param contact_id: int: Identify the contact to be removed
    :param db: Session: Pass the database session to the function
    :return: The contact that was deleted
    :doc-author: Trelent
    """
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
