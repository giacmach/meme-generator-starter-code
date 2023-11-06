"""Build CSVIngestor.

Ingest and parse.
"""
import os
import pandas as pd

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Build CSVIngestor.

    Ingest and parse.
    """

    def can_ingest(self, path: str):
        """Return a boolean file is can ingest."""
        if path and path.endswith('.csv') and os.path.isfile(path):
            return True
        return False

    def parse(self, path: str):
        """Return a list result."""
        result = []

        csv_data = pd.read_csv(path)
        if csv_data is not None:
            data_dict = csv_data.to_dict('records')
            for quote_dict in data_dict:
                result.append(QuoteModel(body=quote_dict.get('body'), author=quote_dict.get('author')))

        return result
