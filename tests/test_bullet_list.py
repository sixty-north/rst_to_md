from test_util import rst_to_md


def test_basic_bullet_list():
    rst = """- llamas
- emus
- yaks"""

    expected = """- llamas

- emus

- yaks

"""

    md = rst_to_md(rst)

    assert md == expected


def test_list_item_with_bold():
    rst = """\
- llamas
- emus
- yaks **are** fuzzy"""

    expected = """\
- llamas

- emus

- yaks **are** fuzzy

"""

    md = rst_to_md(rst)

    assert md == expected


def test_multiline_list_item():
    rst = """\
- llamas. Foo
  bar baz.
- emus
- yaks **are** fuzzy"""

    expected = """\
- llamas. Foo
  bar baz.

- emus

- yaks **are** fuzzy

"""

    md = rst_to_md(rst)

    assert md == expected


def test_multiparagraph_list_item():
    rst = """\
- llamas. Foo
  bar baz.

  Fnord fnord fnord.

- emus
- yaks **are** fuzzy"""

    expected = """\
- llamas. Foo
  bar baz.

  Fnord fnord fnord.

- emus

- yaks **are** fuzzy

"""

    md = rst_to_md(rst)

    assert md == expected


def test_nested_bullet_list():
    rst = """\
- point
- point

  - sub-point
  - sub-point **2**

    - sub-**sub**-point
    - and so forth
"""

    expected = """\
- point

- point

  - sub-point

  - sub-point **2**

    - sub-**sub**-point

    - and so forth

"""

    md = rst_to_md(rst)

    assert md == expected
