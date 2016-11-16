# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['test_app']

test_app = Blueprint('test_app', __name__)


@test_app.route('/')
def index():
    return "Hello World!"
