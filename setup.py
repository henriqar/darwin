#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

opt_extension = Extension(
    name='_opt',
    sources=['darwin/_opt.c']
)

setup(
    name="darwin",
    version="0.0.0",
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
    ext_modules=[opt_extension]
)
