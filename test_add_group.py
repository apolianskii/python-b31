# -*- coding: utf-8 -*-
from application import Application
from group import Group

import unittest

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_group(self):
        self.app.log_in(username="admin", password="secret")
        self.app.create_group(Group(name="Test", header="Test", footer="Test"))
        self.app.log_out()

    def test_add_empty_group(self):
        self.app.log_in(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.log_out()
    
    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
