#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='easy-selenium',
    version='0.1.1',
    description='Tool to make the use of selenium easier',
    author='Tiago Lira',
    author_email='tiagoliradsantos@gmail.com',
    license='MIT',
    url='https://github.com/Tiago-Lira/easy-selenium.git',
    download_url='https://github.com/Tiago-Lira/easy-selenium/tarball/0.1.0',
    keywords=['selenium', 'wrapper', 'easy', 'selenium-wrapper'],
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
)
