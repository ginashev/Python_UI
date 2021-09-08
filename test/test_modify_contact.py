from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fName="Fname", lName="Lname", title="Director", company="Test", address_1="Address 1",
                               hPhone="+38093123123", mPhone="+38093568229",
                               email="test@test.com", bDay="1", bMonth="August", bYear="1985", address_2="Address 2",
                               notes="testUser", homepage="test.test.com"))
    contact = Contact(fName="Fname2", lName="Lname2", title="Director2", company="Test2", address_1="Address 12",
                                             hPhone="+380931231232", mPhone="+380935682292",
                                             email="test@test.com2", bDay="12", bMonth="September", bYear="1996", address_2="Address 22",
                                             notes="testUser2", homepage="test2.test.com")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

