#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kales',
    version='0.1',
    author='Timothée Peignier',
    author_email='timothee.peignier@tryphon.org',
    description='Python client to the OpenCalais API',
    url='http://github.com/cyberdelia/kales',
    license=license,
    keywords="opencalais calais",
    py_modules=['kales'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    install_requires=[
        "requests>=0.11"
    ]
)