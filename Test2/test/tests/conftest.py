# -*- coding: utf-8 -*-
import pytest

from Test2 import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
