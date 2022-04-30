# -*- coding: utf-8 -*-
import pytest

from application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.log_in(username="admin", password="secret")
    app.create_group(Group(name="Test", header="Test", footer="Test"))
    app.log_out()


def test_add_empty_group(app):
    app.log_in(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.log_out()
