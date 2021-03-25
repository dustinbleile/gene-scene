"""Install python requirements and packages.

Suggested to create an isolated virtual environment first:
    python3 -m venv venv

Activate the environment:
    source venv/bin/activate

Then make sure pip and setuptools are up to date:
    python -m pip install -U pip setuptools wheel

Standard installation:
    python -m pip install -U -e .

Developer installation:
    python -m pip install -U -e .[dev]
"""

import codecs
import os

from setuptools import find_packages, setup

name = "gene_scene"

INSTALL_REQS = [
    "jupyter",
    "logzero",
    "numpy",
    "pandas",
]

# Dependencies required for development
DEV_REQS = ["flake8", "black", "isort", "mypy", "pylint", "pydocstyle"]

# Dependencies required only for running tests
TEST_REQS = ["pytest", "pytest-cov"]

# Dependencies required for deploying to an index server
DEPLOYMENT_REQS = [
    "twine",
    "wheel",
]

long_description = ""
long_description_content_type = "text/markdown"

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except Exception:
    pass


def read(rel_path):
    """Safe read local file."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    """Read __version__ property from file."""
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name=name,
    version=get_version(os.path.join(name, "__init__.py")),
    packages=find_packages(),
    install_requires=INSTALL_REQS,
    extras_require={
        "dev": TEST_REQS + DEPLOYMENT_REQS + DEV_REQS,
        "deploy": DEPLOYMENT_REQS,
        "test": TEST_REQS,
    },
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    python_requires=">=3.8",
    dependency_links=[],
    test_suite="tests",
    tests_require=TEST_REQS,
)
