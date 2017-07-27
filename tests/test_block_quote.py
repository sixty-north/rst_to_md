from test_util import rst_to_md


def test_basic_block_quote():
    rst = """

    This is a test.
    Only a test.

"""

    expected = """> This is a test.
> Only a test.


"""

    md = rst_to_md(rst)
    assert md == expected


def test_inline_elements():
    rst = """

    This is **a** test.
    Only a test."""

    expected = """\
> This is **a** test.
> Only a test.


"""

    md = rst_to_md(rst)
    assert md == expected
