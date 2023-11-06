"""TextIngestor class."""
import os
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """A TextIngestor class."""

    def can_ingest(self, path: str):
        """Return a boolean."""
        if path and path.endswith('.txt') and os.path.isfile(path):
            return True
        return False

    def parse(self, path: str):
        """Return a list quote model."""
        result = []
        with open(path, 'r') as txt_file:
            txt_contents = txt_file.read()
            txt_contents_list = txt_contents.split('\n')
            for text in txt_contents_list:
                text_list = text.split(' - ')
                if len(text_list) == 1:
                    quote_model_instance = QuoteModel(body=text)
                else:
                    quote_model_instance = QuoteModel(body=text_list[0], author=text_list[1])
                result.append(quote_model_instance)
        return result
