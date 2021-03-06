#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def get_packages(package):
    return [dirpath for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-treasuremap',
    version='0.2.3',
    url='https://github.com/silentsokolov/django-treasuremap',
    license='MIT',
    author='Dmitriy Sokolov',
    author_email='silentsokolov@gmail.com',
    description='django-treasuremap app, makes it easy to store and display '
                'the location on the map using different providers (Google, Yandex).',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    packages=get_packages('treasuremap'),
    package_data=get_package_data('treasuremap'),
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
