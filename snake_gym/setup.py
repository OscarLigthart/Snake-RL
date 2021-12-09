#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='snake_gym',
    version='v1.0.0',
    description="An OpenAI gym wrapper around a pygame implementation of Snake",
    author='Oscar Ligthart',
    author_email='oscarligthart@gmail.com',
    packages=find_packages(include=['snake_gym', 'snake_gym.*']),
    install_requires=[
        'pygame==2.1.0',
        'numpy'
    ],
)
