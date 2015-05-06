import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="awsexpire",
    version="0.0.1",
    author="Ellis Percival",
    author_email="awsexpire@failcode.co.uk",
    description="",
    license="UNLICENSE",
    keywords="aws boto ec2 rds",
    url="https://github.com/flyte/aws-expire",
    packages=("awsexpire",),
    install_requires=read("requirements.txt"),
    entry_points={
        "console_scripts": (
            "awsexpire = awsexpire.tool:main",
        )
    }
)