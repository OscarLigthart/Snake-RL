#!/usr/bin/env python3

from setuptools import setup, find_packages
with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='snake_gym',
    version='v1.0.0',
    description="An OpenAI gym wrapper around a pygame implementation of Snake",
    author='Oscar Ligthart',
    author_email='oscarligthart@gmail.com',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    packages=find_packages(include=['snake_gym', 'snake_gym.*']),
    entry_points={"console_scripts": ["snake-gym-demo = snake_gym.__main__:main"]}
)

