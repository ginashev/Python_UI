from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(fName="Fname", lName="Lname", title="Director", company="Test", address_1="Address 1",
                               hPhone="+38093123123", mPhone="+38093568229",
                               email="test@test.com", bDay="1", bMonth="August", bYear="1985", address_2="Address 2",
                               notes="testUser", homepage="test.test.com"))


def test_empty_contact(app):
    app.contact.create_empty()
