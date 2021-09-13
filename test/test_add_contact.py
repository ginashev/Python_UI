from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digital_for_phone(maxlen):
    symbols = string.digits + "-" + "+"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_for_email(maxlen):
    nickname = "".join([random.choice(string.ascii_letters + string.digits) for i in
                        range(random.randrange(maxlen))])
    domain = "".join([random.choice(string.ascii_letters + string.digits + "-") for i in
                      range(random.randrange(maxlen))])
    cctld = "".join([random.choice(string.ascii_letters + "."*10) for i in range(random.randrange(5))])
    return nickname + "@" + domain + cctld


testdata = [Contact(firstname="", lastname="", address="", email="", email2="",
                    email3="", homephone="", mobilephone="", workphone="", secondaryphone="")] + [
               Contact(firstname=random_string("name", 10), lastname=random_string("lastname", 10),
                       address=random_string("address", 10),
                       email=random_string_for_email(10), email2=random_string_for_email(10),
                       email3=random_string_for_email(10), homephone=random_digital_for_phone(10),
                       mobilephone=random_digital_for_phone(10), workphone=random_digital_for_phone(10),
                       secondaryphone=random_digital_for_phone(10))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
