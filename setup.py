# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from Test2 import __version__


setup(
    name="Test2",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["Test2", "Test2.test"],
    platforms=["any"]
)
