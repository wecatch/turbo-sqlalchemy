#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='turbo_sqlalchemy',
    version='0.0.1',
    description="Turbo sqlalchemy plugin",
    long_description=readme + '\n\n' + history,
    author="wecatch",
    author_email='wecatch.me@gmail.com',
    url='https://github.com/wecatch/turbo_sqlalchemy',
    packages=[
        'turbo_sqlalchemy',
    ],
    package_dir={'turbo_sqlalchemy':
                 'turbo_sqlalchemy'},
    entry_points={
        'console_scripts': [
            'turbo_sqlalchemy=turbo_sqlalchemy.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='turbo_sqlalchemy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
