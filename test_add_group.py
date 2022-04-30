# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from group import Group

import unittest

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd
        self.log_in(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="Test", header="Test", footer="Test"))
        self.log_out(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.log_in(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.log_out(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def log_in(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def open_groups_page_after_creation(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.open_groups_page_after_creation(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
