# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(fName="Fname", lName="Lname", title="Director", company="Test", address_1="Address 1",
                               hPhone="+38093123123", mPhone="+38093568229",
                               email="test@test.com", bDay="1", bMonth="August", bYear="1985", address_2="Address 2",
                               notes="testUser", homepage="test.test.com"))
    app.session.logout()