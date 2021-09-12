from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First_name", lastname="Last_name", address="Address_line",
                      email="test1@text.com", email2="test2@text.com", email3="test3@text.com",
                      homephone="12345", mobilephone="23451", workphone="34512", secondaryphone="45123")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_empty_contact(app):
#     app.contact.create_empty()
