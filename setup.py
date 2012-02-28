#!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

from setuptools import setup

setup(
    name='django-testing-fixes',
    version='0.0.1',
    description='A set of fixes for various broken things about django testing.',
    long_description=open('README.rst').read(),
    author="Tim 'mithro' Ansell",
    author_email='mithro@mithis.com',
    url='https://github.com/mithro/django-testing-fixes',
    download_url='https://github.com/mithro/django-testing-fixes/downloads',
    license='BSD',
    packages=["django_testing_fixes"],
    test_suite='tests',
    tests_require=[
        'django>=1.3,<1.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
