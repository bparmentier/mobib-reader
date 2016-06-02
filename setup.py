#!/usr/bin/env python

from setuptools import setup

setup(
    name='mobib',
    version='0.1',
    description='Retrieve remaining number of trips from your MOBIB Basic',
    author='Bruno Parmentier',
    author_email='dev@brunoparmentier.be',
    url='https://github.com/bparmentier/mobib-reader/',
    py_modules=['mobib'],
    entry_points={
        'console_scripts': ['mobib = mobib:main']
    }
)
