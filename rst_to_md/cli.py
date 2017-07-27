from docutils.core import default_description, publish_cmdline

from .converter import Writer


def main():
    description = ('Generates Markdown from standalone reStructuredText sources.  ' + default_description)
    publish_cmdline(writer=Writer(), description=description)


if __name__ == '__main__':
    main()
