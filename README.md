# rst_to_md

A Markdown writer for Docutils.

This writer lets you convert reStructuredText documents to Markdown with
Docutils. The package includes a writer and translator along with a command-line
tool for doing conversions.

This was originally developed to support Sixty North's publication efforts, so
it may have behaviors that are specific to those needs. However, it should be
generally useful for rst-to-md conversion.

## Quick start

```
$ python setup.py install
$ rst-to-md my_doc.rst > my_doc.md
```
