# -*- coding: utf-8 -*-
import datetime

from model.contact import Contact


def test_add_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.contact.create(get_filled_contact())
    app.session.log_out()


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
