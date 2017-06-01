Bloomfilters4py3
================

A Bloomfilter implement in pure python for python3.

Package Installation and Usage
------------------------------

The package is available on PyPI:

    pip install bloomfilter4py3

The library can be imported in the usual way:

    import bloomfilter

APIs
----

Bloomfilter(nBits, nHashs)
    Return a Bloomfilter object with bucket length of nBits and nHashs hash functions.

Bloomfilter(filepath)
    Return a Bloomfilter object that read from file at filepath.

Bloomfilter.save(filepath)
    Save the filter in file at filepath.

Bloomfilter.add(str)
    Add str to the filter.

Bloomfilter.test(str)
    Return a True if str might in the filter.