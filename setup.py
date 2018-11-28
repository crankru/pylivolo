from setuptools import setup, find_packages

PACKAGE = ""
NAME = "pylivolo"
DESCRIPTION = ""
AUTHOR = "Crank"
AUTHOR_EMAIL = "crank@crank.ru"
URL = "https://github.com/crankru/pylivolo"
# VERSION = __import__(PACKAGE).__version__
VERSION = 0.1
 
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests", 'blynk.py']),
    # install_requires=[],
    # package_data=find_package_data(
    #     PACKAGE,
    #     only_in_packages=False
    # ),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)