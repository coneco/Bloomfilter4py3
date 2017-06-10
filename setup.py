from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bloomfilter4py3',
    version='1.1.1',
    description='A Bloomfilter implement in pure python for python3.',
    long_description=long_description,
    url='https://github.com/coneco/Bloomfilter4py3',
    author='coNEco',
    author_email='coneco@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='bloomfilter',
    packages = ['bloomfilter'],
    install_requires=['py3bitlist'],
    extras_require={
        'dev': [],
        'test': [],
    }
)