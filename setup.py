#!/usr/bin/env python3
"""Setup script for BrutePy."""

from setuptools import setup
import os

# Read the README for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="brutepy",
    version="2.1.0",
    author="wjdavis5",
    description="Modern HTTP Basic Authentication brute force tool for penetration testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjdavis5/BrutePy",
    py_modules=["Brute"],
    python_requires=">=3.6",
    install_requires=requirements,
    scripts=["Brute.py"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    keywords="security penetration-testing brute-force http-auth",
    project_urls={
        "Bug Reports": "https://github.com/wjdavis5/BrutePy/issues",
        "Source": "https://github.com/wjdavis5/BrutePy",
    },
)
