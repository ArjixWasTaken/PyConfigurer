# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md", "r").read()
except IOError:
    long_description = ""

try:
    requirements = [x.strip() for x in open(
        "requirements.txt", "r").read().split("\n") if x.strip()]
except IOError:
    requirements = []

setup(
    name="PyConfigurer",
    version="0.0.1",
    description="A GUI configuration library for python programs.",
    license="MIT",
    author="ArjixWasTaken",
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
