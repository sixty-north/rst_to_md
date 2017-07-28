# rst_to_md

[![Build Status](https://travis-ci.org/sixty-north/rst_to_md.png?branch=master)]

A Markdown writer for Docutils.

This writer lets you convert reStructuredText documents to Markdown with
Docutils. The package includes a writer and translator along with a command-line
tool for doing conversions.

This was originally developed to support Sixty North's publication efforts, so
it may have behaviors that are specific to those needs. However, it should be
generally useful for rst-to-md conversion.

This project is based on Chris
Wrench's [rst2md project](https://github.com/cgwrench/rst2md).

## Quick start

```
$ python setup.py install
$ rst-to-md my_doc.rst > my_doc.md
```

## How to use for Leanpub publication

The main reason we created this tool is to support our Leanpub work which
involves a lot of reStructuredText-to-Markdown conversion. In general you can
use `rst-to-md` to directly convert our `*.rst` sources to `*.md` like this:

```
rst-to-md module_1.rst > chapter_1.md
```

It's possible that your rst source contains elements which our translator
doesn't support. If so you'll see something like this:

```
rst-to-md module_1.rst > chapter_1.md
module_1.rst:: (WARNING/2) The doctest_block element is not supported.
module_1.rst:: (WARNING/2) The bullet_list element is not supported.
```

In that case, you probably need to update `rst_to_md/translator.py` to handle
those elements. Generally this is very straightforward, and you can see all of
the existing examples to get insight.

## Tests

There are a few unit tests for tricky parts of the implementation. First install
the necessary dependencies:

```
$ pip install -e ".[test]"
```

Run the tests with pytest:

```
$ pytest tests
```
