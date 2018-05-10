from test_util import rst_to_md


def test_python_code_block():
    rst = """\
Some code::

  def foo():
      return 1

Good stuff!
"""

    expected = """\
Some code:

{language=python}
~~~~~~~~
def foo():
    return 1
~~~~~~~~

Good stuff!

"""

    md = rst_to_md(rst)
    assert md == expected


def test_pycon_code_block():
    rst = """\
Some code::

  >>> x = 1
  1

Good stuff!
"""

    expected = """\
Some code:

{language=pycon}
~~~~~~~~
>>> x = 1
1
~~~~~~~~

Good stuff!

"""

    md = rst_to_md(rst)
    assert md == expected


def test_javascript_code_block():
    """
    Common Doctils extensions allow non-python language specification
    using ``code`` and `code-block`` directives.

    Refs:

    * http://www.sphinx-doc.org/en/stable/markup/code.html
    * http://docs.getpelican.com/en/stable/content.html#syntax-highlighting
    """
    rst = """\
Some code:

.. code:: javascript

  x=1;

Good stuff!
"""

    expected = """\
Some code:

{language=javascript}
~~~~~~~~
x=1;
~~~~~~~~

Good stuff!

"""

    md = rst_to_md(rst)
    assert md == expected
