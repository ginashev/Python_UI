# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_conctact_page(wd)
        self.create_contact(wd, Contact(fName="Fname", lName="Lname", title="Director", company="Test", address_1="Address 1",
                            hPhone="+38093123123", mPhone="+38093568229",
                            email="test@test.com", bDay="1", bMonth="August", bYear="1985", address_2="Address 2",
                            notes="testUser", homepage="test.test.com"))
        self.open_home_page_from_menu(wd)
        self.logout(wd)

    def create_contact(self, wd, contact):
        wd.find_element_by_name("firstname").send_keys(contact.fName)
        wd.find_element_by_name("lastname").send_keys(contact.lName)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address_1)
        wd.find_element_by_name("home").send_keys(contact.hPhone)
        wd.find_element_by_name("mobile").send_keys(contact.mPhone)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bDay)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bMonth)
        wd.find_element_by_xpath("//option[@value='" + contact.bMonth + "']").click()
        wd.find_element_by_name("byear").send_keys(contact.bYear)
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_css_selector("input[type=submit]:last-child").click()

    def open_add_conctact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()

    #        self.assertEqual([], self.verificationErrors)

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def open_home_page_from_menu(self, wd):
        wd.find_element_by_link_text("home page").click()


if __name__ == "__main__":
    unittest.main()
