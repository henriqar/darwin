#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.util import convert_path

# get version information
metadata = {}
ver_path = convert_path('darwin/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), metadata)

setup(
    name="darwin",
    version=metadata['__version__'],
    author="Henrique A. Rusa",
    author_email="henrique.rusa@gmail.com",
    description="",
    license="MIT",
    keywords="",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License"
    ],
)
