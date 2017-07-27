from docutils.core import publish_parts


from rst_to_md.writer import Writer


def rst_to_md(rst):
    parts = publish_parts(source=rst,
                          writer=Writer())
    return parts["whole"]


def test_basic_block_quote():
    rst = """

    This is a test.
    Only a test.
"""

    expected = """
> This is a test.
> Only a test.

"""

    md = rst_to_md(rst)
    assert md == expected


def _test_inline_elements():
    rst = """

    This is **a** test.
    Only a test.
"""

    expected = """
> This is **a** test.
> Only a test.

"""

    md = rst_to_md(rst)
    assert md == expected
