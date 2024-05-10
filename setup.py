from setuptools import setup, find_packages
import codecs
import os


VERSION = "0.1.0"
DESCRIPTION = "Get IP addresses from a website using Selenium and Chrome WebDriver"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="IPAdresseScraping",
    version=VERSION,
    author="abdelazizeeeee",
    author_email="abdelaziz.naija@horizon-tech.tn",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=requirements,
    keywords=["python", "IP", "Selenium", "WebDriver", "Scraping"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
