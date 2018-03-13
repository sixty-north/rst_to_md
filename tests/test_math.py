from test_util import rst_to_md


def test_basic_block_quote():
    rst = """

Here is block math

.. math::

    x^2
"""

    expected = """Here is block math

$$x^2$$
"""

    md = rst_to_md(rst)
    assert md == expected


def test_inline_elements():
    rst = """

    Here is inline math :math:`x^2`.
"""

    expected = """\
Here is inline math $x^2$.

"""

    md = rst_to_md(rst)
    assert md == expected
