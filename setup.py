#!/usr/bin/env python

from setuptools import setup, find_packages
from pathlib import Path


'''
setup module for core.
Created on 5/20/2020
@author: songlin.xiesl、guangling.zgl
'''
NAME = "global_open_sdk_python"
DESCRIPTION = "The global alipay gateway SDK for Python."
AUTHOR = "songlin.xiesl"
AUTHOR_EMAIL = "songlin.xiesl@alibaba-inc.com"
URL = "https://github.com/alipay/global-open-sdk-python"
VERSION = "1.0.0"
'''
only python2 need enum34、pytz
'''
requires = ["enum34", "pytz", "pycryptodome", "rsa"]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    keywords=["global", "alipay", "sdk"],
    packages=find_packages(where='*'),
    include_package_data=True,
    platforms='any',
    install_requires=requires,
    classifiers=(
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    )
)
