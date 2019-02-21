# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Orion Context Broker Python integration',
    long_description=readme,
    author='Everton de Matos',
    author_email='everton.matos@imed.edu.br',
    url='https://github.com/evermatos/orion_integration',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
