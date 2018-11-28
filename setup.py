from setuptools import setup, find_packages

PACKAGE = ""
NAME = "pylivolo"
DESCRIPTION = ""
AUTHOR = "Crank"
AUTHOR_EMAIL = "crank@crank.ru"
URL = "https://github.com/crankru/pylivolo"
# VERSION = __import__(PACKAGE).__version__
VERSION = '0.1.1'

with open("README.md", "r") as fh:
    long_description = fh.read()
 
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    # install_requires=[],
    # package_data=find_package_data(
    #     PACKAGE,
    #     only_in_packages=False
    # ),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Raspbian",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)