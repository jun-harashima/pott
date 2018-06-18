#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import pip
from setuptools import setup, find_packages
from pip.req import parse_requirements

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ str(requirement.req) for requirement in parse_requirements('requirements_dev.txt', session = pip.download.PipSession()) ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jun Harashima",
    author_email='j.harashima@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="paper organization tool on terminal",
    entry_points={
        'console_scripts': [
            'pott=pott.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pott',
    name='pott',
    packages=find_packages(include=['pott', 'pott.assistants', 'pott.files', 'pott.utils']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jun-harashima/pott',
    version='0.1.0',
    zip_safe=False,
)
