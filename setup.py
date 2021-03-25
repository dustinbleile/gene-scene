from setuptools import find_packages, setup

# Dependencies required to use your package
INSTALL_REQS = [
    "jupyter",
]

# Dependencies required for development
DEV_REQS = ["flake8", "black", "isort", "mypy", "pylint"]

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

setup(
    name="gene_scene",
    version="0.0.0",
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
