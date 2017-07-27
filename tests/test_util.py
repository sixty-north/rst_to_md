from docutils.core import publish_parts


from rst_to_md.writer import Writer


def rst_to_md(rst):
    parts = publish_parts(source=rst,
                          writer=Writer())
    return parts["whole"]
