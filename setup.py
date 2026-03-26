#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from smoothlogging.version import __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest",
    "pytest-cov"
]

setup(
    name='smoothlogging',
    version=__version__,
    description="smoothlogging helps to log easily to file with timestamp + standard output",
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
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
