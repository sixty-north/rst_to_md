from test_util import rst_to_md


def test_simple_paragraph():
    rst = """Some goes here. Maybe
some text with line breaks as well. Who know?
It's all quite a mystery.
"""

    expected = rst

    md = rst_to_md(rst)
    assert md == expected
