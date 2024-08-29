"""
bpm2fps - Convert beats per minute to animation frames.
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="bpm2fps",
    version="1.0.2",
    description="Convert beats per minute to animation frames.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/BreadMakesYouFull/bpm2fps.git",
    author="BreadMakesYouFull",
    license="MIT",
    classifiers=[
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License"
    ],
    keywords="fps bpm calculate calculator usd animation anim reference",
    packages=find_packages(),
    extras_require = {
        'gui':  ["pyside6"]
    },
    package_data={
        "": ["*.qml"]
    },
    entry_points={
        'console_scripts': [
            'bpm2fps=bpm2fps.cli:main',
        ],
    },
)
