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