#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from smoothlogging.version import VERSION

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "logging"
]

test_requirements = [
    "pytest",
    "pytest-cov"
]

setup(
    name='smoothlogging',
    version=VERSION,
    description="Handy modules, starting with smoothlogging to manage logging with files in just a few lines.",
    long_description=readme + '\n\n' + history,
    author="Sebastian Blasiak",
    author_email='sebastian.blasiak@gmail.com',
    url='https://github.com/blasebast/smoothlogging',
    packages=[
        'smoothlogging',
    ],
    package_dir={'smoothlogging':'smoothlogging'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='sebastian, blasiak, logging, smoothlogging, logfile',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
