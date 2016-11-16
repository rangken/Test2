# -*- coding: utf-8 -*-
from flask import url_for


def test_test_index(client):
    res = client.get(url_for('test_app.index'))
    assert res.data == b'Hello World!'
