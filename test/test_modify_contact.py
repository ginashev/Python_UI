from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First_name", lastname="Last_name", address="Address_line",
                                   email="test1@text.com", email2="test2@text.com", email3="test3@text.com",
                                   homephone="12345", mobilephone="23451", workphone="34512", secondaryphone="45123"))
    contact = (Contact(firstname="First_name1", lastname="Last_name1", address="Address_line1",
                                   email="test1@text.com1", email2="test2@text.com1", email3="test3@text.com1",
                                   homephone="123451", mobilephone="234511", workphone="345121", secondaryphone="451231"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

