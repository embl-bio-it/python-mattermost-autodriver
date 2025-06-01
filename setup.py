#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup, find_packages

full_version = ''

root_dir = os.path.abspath(os.path.dirname(__file__))

readme_file = os.path.join(root_dir, 'README.rst')
with open(readme_file, encoding='utf-8') as f:
    long_description = f.read()

version_module = os.path.join(root_dir, 'src', 'mattermostautodriver', 'version.py')
with open(version_module, encoding='utf-8') as f:
    exec(f.read())

setup(
    name='mattermostautodriver',
    version=full_version,
    description='A Python Mattermost Auto Driver',
    long_description=long_description,
    url='https://github.com/embl-bio-it/python-mattermost-autodriver',
    author='Renato Alves, Christian Plümer',
    author_email='bio-it@embl.de, github@kuuku.net',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires=">=3.10",
    install_requires=[
        'aiohttp>=3.9.5,<4.0.0',
        'httpx~=0.28.1',
    ],
)
