import sys
from setuptools import setup

if sys.version_info < (3,0):
    raise ValueError('The censusnotebooks Package requires a Python version greater than 3.0')

with open('requirements.txt') as fid:
    install_requires = [l.strip() for l in fid.readlines() if l]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="censusnotebooks",
    packages=['censusnotebooks'],
    version="0.0.1",
    author="Sandeep Sainath, Yuyang Zhong",
    author_email="author@example.com",
    description="Discovering US Census: Jyputer Notebook Curriculum Modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuyang-zhong/census-notebooks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
