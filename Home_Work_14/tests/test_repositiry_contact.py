from datetime import date
import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel
from src.repository.contact import get_contact, get_contact_by_id, create, remove, update


class TestContactRepository(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1, email='test@test.com')

    async def test_get_contact(self):
        contact = [Contact(), Contact(), Contact()]
        self.session.query(Contact).limit().offset().all.return_value = contact
        result = await get_contact(10, 0, self.session)
        self.assertEqual(result, contact)

    async def test_create_contact(self):
        body = ContactModel(
            first_name='John',
            last_name='Smith',
            phone_number=380998877666,
            birthday=date.today(),
            email='example@test.com',
            additional_data='This my contact'
        )
        result = await create(body, self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.phone_number, body.phone_number)
        self.assertEqual(result.birthday, body.birthday)
        self.assertEqual(result.email, body.email)
        self.assertTrue(hasattr(result, 'id'))

    async def test_get_contact_by_id(self):
        contact = Contact()
        self.session.query().filter_by().first.return_value = contact
        result = await get_contact_by_id(1, self.session)
        self.assertIsInstance(result, Contact)
        self.assertEqual(result.id, contact.id)

    async def test_get_contact_not_found(self):
        self.session.query().filter_by().first.return_value = None
        result = await get_contact_by_id(1, db=self.session)
        self.assertIsNone(result)

    async def test_remove_contact_found(self):
        contact = Contact()
        self.session.query().filter_by().first.return_value = contact
        result = await remove(contact_id=1, db=self.session)
        self.assertEqual(result, contact)

    async def test_remove_contact_not_found(self):
        self.session.query().filter_by().first.return_value = None
        result = await remove(1, db=self.session)
        self.assertIsNone(result)

    async def test_update_contact_found(self):
        body = ContactModel(
            first_name='John',
            last_name='Smith',
            phone_number=380998877666,
            birthday=date.today(),
            email='example@test.com',
            additional_data='This my contact'
        )
        self.session.commit.return_value = None
        result = await update(1, body=body, db=self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.phone_number, body.phone_number)
        self.assertEqual(result.birthday, body.birthday)
        self.assertEqual(result.email, body.email)

    async def test_update_contact_not_found(self):
        body = ContactModel(
            first_name='John',
            last_name='Smith',
            phone_number=380998877666,
            birthday=date.today(),
            email='example@test.com',
            additional_data='This my contact'
        )
        self.session.query().filter_by().first.return_value = None
        self.session.commit.return_value = None
        result = await update(1, body=body, db=self.session)
        self.assertIsNone(result)





