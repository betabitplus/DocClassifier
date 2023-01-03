# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "DocumentClassifier"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="This service classifies documents",
    author="Stanislav Avramenko",
    author_email="betabitpro@gmail.com",
    url="https://github.com/betabitplus/doc_classifier",
    keywords="image document classification service",
    packages=find_packages(),
    long_description=open('README.md').read()
)