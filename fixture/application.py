import locale

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()
        locale.setlocale(locale.LC_ALL, '')
