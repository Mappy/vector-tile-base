#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="vector_tile_base",
    version="1.0.5",
    description="Python implementation of Mapbox vector tiles",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sean Gillies",
    author_email="sean@mapbox.com",
    license="BSD-3-Clause",
    keywords=["vector", "tiles", "mapbox", "protobuf"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.9",
    packages=find_packages(),
    install_requires=[
        "protobuf>=3.20.0",
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    include_package_data=True,
    package_data={
        "vector_tile_base": ["*.proto"],
    },
) 