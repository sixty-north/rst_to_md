from docutils.core import default_description, publish_cmdline

from .writer import Writer


def main():
    description = 'Generates Markdown from standalone '\
                  'reStructuredText sources. {}'.format(
                      default_description)
    publish_cmdline(writer=Writer(), description=description)


if __name__ == '__main__':
    main()
