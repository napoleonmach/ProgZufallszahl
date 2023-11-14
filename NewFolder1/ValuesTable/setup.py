
"""
setup file for project ValuesTable
"""

from pathlib import Path
from setuptools import setup

def read(fname):
    f_path = Path(__file__).parent / fname
    return f_path.read_text()


setup(
    name="tablevalues",
    version="0.0.1",
    # replace underline characters by spaces
    author="Leo",
    author_email="Vorname.Nachname@gmail.com",
    description=("A very simple setup.py file"),
    license="GPL",
    keywords="example",
    url="http://myUrl.com",
    packages=["tablevalues"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Demonstration",
        "License :: GPL License",
    ],
    python_requires=">=3.10, <4",
    install_requires=["setuptools>=60"],
    entry_points=dict(console_scripts= [
            "calctable=tablevalues.main:calc",
        ]
    ),
)
