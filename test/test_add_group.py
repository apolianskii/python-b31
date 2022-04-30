# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.create(Group(name="Test", header="Test", footer="Test"))
    app.session.log_out()


def test_add_empty_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.log_out()
