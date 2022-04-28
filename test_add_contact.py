# -*- coding: utf-8 -*-
import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from contact import Contact

import locale
import unittest

def get_filled_contact():
    contact = Contact()
    contact.first_name = "George"
    contact.middle_name = "Jr."
    contact.last_name = "Plush"
    contact.nickname = "Plushie"
    contact.title = "Mr."
    contact.company_name = "Bright House"
    contact.address = "Bright House, 1500 Transylvania Avenue, S.E., Washington, DC 20500"
    contact.home_phone = "555-123-4567"
    contact.mobile_phone = "555-234-5678"
    contact.work_phone = "555-345-6789"
    contact.fax_phone = "555-456-7890"
    contact.email = "contact@brighthouse.qa"
    contact.email_2 = "contact2@brighthouse.qa"
    contact.email_3 = "contact3@brighthouse.qa"
    contact.homepage = "https://www.brighthouse.qa"
    contact.birthday = datetime.date(year=1992, month=8, day=31)
    contact.anniversary = datetime.date(year=2012, month=12, day=1)
    contact.address_secondary = \
        "QA Department of Python, Office of Inspector General, DEV-62, 1800 Moore Law Street, Arlington, VA 22209"
    contact.home_phone_secondary = "555-098-1234"
    contact.notes = "This contact was created by an automated Python test!"
    return contact

class test_add_contact(unittest.TestCase):
    def setUp(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.log_in(driver, username="admin", password="secret")
        self.open_contacts_page(driver)
        self.create_contact(driver, contact=get_filled_contact())
        self.open_contacts_page_after_creation(driver)
        self.log_out(driver)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def log_in(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def log_out(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def open_contacts_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def open_contacts_page_after_creation(self, driver):
        driver.find_element_by_link_text("home page").click()

    def create_contact(self, driver, contact):
        # init contact creation
        driver.find_element_by_link_text("add new").click()
        # fill contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middle_name)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company_name)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home_phone)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work_phone)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax_phone)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email_2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email_3)
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.homepage)
        driver.find_element_by_name("bday").click()
        driver.find_element_by_xpath("//select[@name='bday']/option[@value='{}']".format(
            str(contact.birthday.day))).click()
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_xpath("//select[@name='bmonth']/option[@value='{}']".format(
            contact.birthday.strftime("%B"))).click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(str(contact.birthday.year))
        driver.find_element_by_name("aday").click()
        driver.find_element_by_xpath("//select[@name='aday']/option[@value='{}']".format(
            str(contact.anniversary.day))).click()
        driver.find_element_by_name("amonth").click()
        driver.find_element_by_xpath("//select[@name='amonth']/option[@value='{}']".format(
            contact.anniversary.strftime("%B"))).click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(str(contact.anniversary.year))
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address_secondary)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.home_phone_secondary)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        driver.find_element_by_name("submit").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
        locale.setlocale(locale.LC_ALL, '')

if __name__ == "__main__":
    unittest.main()
