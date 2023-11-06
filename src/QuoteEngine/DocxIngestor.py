"""Build DocxIngestor.

Ingest and parse.
"""
import docx
import os
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Build DocxIngestor.

    Ingest and parse.
    """

    def can_ingest(self, path: str):
        """Return a boolean file is can ingest."""
        return self.is_docx_file(path)

    def parse(self, path: str):
        """Return a list result."""
        try:
            data_docx = docx.Document(path)
            result = []
            for paragraph in data_docx.paragraphs:
                if paragraph.text:
                    text_list = paragraph.text.split(' - ')
                    if len(text_list) == 1:
                        quote_model_instance = QuoteModel(body=paragraph.text)
                    else:
                        quote_model_instance = QuoteModel(body=text_list[0], author=text_list[1])
                    result.append(quote_model_instance)
            return result
        except IOError:
            return []


    def is_docx_file(self, path: str):
        """Return a boolean file is docx or not."""
        if not path:
            return False

        if not path.endswith('.docx'):
            return False

        if os.path.isfile(path):
            return False

        return True