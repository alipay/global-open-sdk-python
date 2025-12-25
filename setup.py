#!/usr/bin/env python

from setuptools import setup, find_packages

"""
setup module for core.
Created on 5/20/2020
@author: songlin.xiesl、guangling.zgl
"""
NAME = "global-open-sdk-python"
DESCRIPTION = "The global alipay gateway SDK for Python."
AUTHOR = "guodong.wzj"
AUTHOR_EMAIL = "wangzunjiao.wzj@digital-engine.com"
URL = "https://github.com/alipay/global-open-sdk-python"
VERSION = "1.4.23"
"""
only python2 need enum34、pytz
"""
requires = ["enum34", "pytz", "pycryptodome", "rsa", "cryptography"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    keywords=["global", "alipay", "sdk"],
    packages=find_packages(exclude=["example"]),
    include_package_data=True,
    platforms="any",
    install_requires=requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
    ],
)
