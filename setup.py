import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Demo of launcher.",
    version="0.0.0",
    author="Matthew Goodman",
    author_email="meawoppl@gmail.com",
    description="An example of how to use the conda launcher.",
    license="BSD",
    url="http://www.github.com/meawoppl/hello-launcher",
    packages=['hello'],
    long_description=read('README.md')
)
