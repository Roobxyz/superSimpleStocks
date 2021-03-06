import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "superSimpleStocks",
        version = "1.0.0",
        author = "Reuben Taylor",
        author_email = "reuben91@me.com",
        description = ("SuperSimpleStocks is a basic OO toy stock exchange"),
        license = "BSD",
        keywords = "superSimpleStocks trading basic",
        packages=['superSimpleStocks', 'test'],
        long_description=read('README.md'),
        classifiers=[
                    "License :: OSI Approved :: BSD License",
                ],
)
