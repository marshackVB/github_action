import setuptools
import os



version_file = open('VERSION')
version = version_file.read().strip()


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "sklearn-transformers",
    version = version,
    author = "Marshall Carter",
    author_email = "carter.marshall@gmail.com",
    desciption = "Custom scikit-learn transfomers",
    long_description = long_description,
    long_destricption_content_type = "text/markdown",
    url = "https://github.com/marshackVB/tranformers",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires = ["pandas", "scikit-learn"],
    python_requires =  ">=3.6"
)