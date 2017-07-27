from docutils import frontend, writers

from .translator import Translator


class Writer(writers.Writer):

    supported = ('markdown',)
    """Formats this writer supports."""

    output = None
    """Final translated form of `document`."""

    # Add configuration settings for additional Markdown flavours here.
    settings_spec = (
        'Markdown-Specific Options',
        None,
        (('Extended Markdown syntax.',
          ['--extended-markdown'],
          {'default': 0, 'action': 'store_true',
           'validator': frontend.validate_boolean}),
         ('Strict Markdown syntax. Default: true',
          ['--strict-markdown'],
          {'default': 1, 'action': 'store_true',
           'validator': frontend.validate_boolean}),))

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = Translator

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()
