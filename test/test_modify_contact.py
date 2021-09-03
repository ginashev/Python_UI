from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(fName="Fname2", lName="Lname2", title="Director2", company="Test2", address_1="Address 12",
                                             hPhone="+380931231232", mPhone="+380935682292",
                                             email="test@test.com2", bDay="12", bMonth="September", bYear="1996", address_2="Address 22",
                                             notes="testUser2", homepage="test2.test.com"))
