from test_util import rst_to_md


def test_bare_uri():
    rst = "http://example.com/llamas"
    expected = "[{0}]({0})\n\n".format(rst)
    md = rst_to_md(rst)
    assert md == expected


def test_named_reference():
    rst = "`some name <http://someuri.io/path>`_"
    expected = "[some name](http://someuri.io/path)\n\n"
    md = rst_to_md(rst)
    assert md == expected
