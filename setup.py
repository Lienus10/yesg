from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='yesg',

    version='2.1.1',

    description='This module downloads the latest and historic esg scores for stocks from Yahoo Finance.',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/Lienus10/yesg',

    author='Julius Langer',

    author_email='julius.langer@outlook.de',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: Office/Business :: Financial :: Investment',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages=find_packages(),

    python_requires='>=3.6, <4',

)
