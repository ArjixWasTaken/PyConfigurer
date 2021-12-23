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
    version="0.0.3",
    description="A GUI configuration library for python programs.",
    license="MIT",
    author="ArjixWasTaken",
    author_email='arjixg53@gmail.com',
    url='https://github.com/ArjixWasTaken/PyConfigurer',
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    keywords=["configuration", "gui"]
)
