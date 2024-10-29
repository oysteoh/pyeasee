"""Setup script for easee"""

import os.path
from setuptools import setup, find_packages

# This call to setup() does all the work
setup(
    name="pyeasee",
    version="0.8.8",
    description="Easee EV charger API library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nordicopen/pyeasee",
    author="Ola Lidholm",
    author_email="olal@plea.se",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["aiohttp", "pysignalr==1.0.0"],
    entry_points={"console_scripts": ["pyeasee=pyeasee.__main__:main"]},
)
