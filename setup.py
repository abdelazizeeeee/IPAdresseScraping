from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.1.0"
DESCRIPTION = (
    "Get IP addresses from a website using Selenium and Chrome WebDriver"
)
LONG_DESCRIPTION = (
    "Get IP addresses from a website using Selenium and Chrome WebDriver"
)
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
# Setting up
setup(
    name="IPAdresseScraping",
    version=VERSION,
    author0="Abdelaziz NAIJA",
    author_email="<abdelaziz.naija@horizon-tech.tn>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
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