from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.open_menu_home()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.fName)
        self.change_field_value("lastname", contact.lName)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address_1)
        self.change_field_value("home", contact.hPhone)
        self.change_field_value("mobile", contact.mPhone)
        self.change_field_value("email", contact.email)
        self.select_field_value("bday", contact.bDay)
        self.select_field_value("bmonth", contact.bMonth)
        self.change_field_value("byear", contact.bYear)
        self.change_field_value("address2", contact.address_2)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("homepage", contact.homepage)

    def select_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_xpath("//option[@value='" + value + "']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_menu_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("a [title='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_menu_home()

    def create_empty(self):
        wd = self.app.wd
        self.open_add_contact_page()
        wd.find_element_by_name("submit").click()
        self.open_menu_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_menu_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_menu_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))
