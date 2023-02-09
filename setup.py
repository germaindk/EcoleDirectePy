from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.4'
DESCRIPTION = 'a API Wrapper for EcoleDirecte.fr'

# Setting up
setup(
    name="EcoleDirectePy",
    version=VERSION,
    author="DK16",
    author_email="<dk16v2@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=codecs.open('README.md', 'r', 'utf-8').read(),
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'ecoledirecte', 'api', 'Wrapper'],
)