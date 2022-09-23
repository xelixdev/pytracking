from itertools import chain

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

EXTRA_REQUIRES = {
    "test": ["tox", "pytest", "pytest-django"],
    "webhook": ["requests>=2.10.0"],
    "html": ["lxml>=4.4.0"],
    "crypto": ["cryptography>=2.0.0"],
    "django": ["django-ipware>=2.0.0", "django>=1.11"],
}

ALL_REQUIRE = list(chain(*EXTRA_REQUIRES.values()))

EXTRA_REQUIRES["all"] = ALL_REQUIRE

setup(
    name="pytracking2",
    version="0.4.4",
    description="Email open and click tracking",
    long_description=long_description,
    url="https://github.com/mikicz/pytracking",
    author="Mikuláš Poul",
    author_email="mikulaspoul@gmail.com",
    license="New BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="email open click tracking",
    packages=find_packages(".", include=("pytracking", "pytracking.*")),
    extras_require=EXTRA_REQUIRES,
    python_requires='>=3.5',
)
