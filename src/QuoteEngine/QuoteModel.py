"""Build QuoteModel.

init and str.
"""
from abc import ABC, abstractmethod


class QuoteModel(ABC):
    """Build QuoteModel.

    init and str.
    """

    def __init__(self, body = '', author = ''):
        """Return a boolean file is can ingest."""
        if body:
            self.body = body
        if author:
            self.author = author

    def __str__(self):
        """Return a boolean file is can ingest."""
        print(f'{self.body} - {self.author}')
