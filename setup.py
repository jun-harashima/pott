#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

readme = """
pott, a paper organization tool on terminal, helps you find papers from the Internet and your PC.

Are you researchers? Or, engineers who are interested in scientific papers? When working on terminal, such as when writing a paper or program, do you ever want to read a related paper? If the paper is not in your PC, you have to leave the terminal, launch a web browser, and find it from the Internet. Even if the paper is, you have to find it from the PC. This is waste of time.

Try pott!
"""

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

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
    version='0.0.2',
    zip_safe=False,
)
