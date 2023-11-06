"""Build PDFIngestor.

init and str.
"""
import os
import subprocess

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from subprocess import PIPE


class PDFIngestor(IngestorInterface):
    """Build PDFIngestor.

    Include can_ingest and parse.
    """

    def can_ingest(self, path: str):
        """Return a boolean file is can ingest."""
        if path and path.endswith('.pdf') and os.path.isfile(path):
            return True
        return False

    def parse(self, path: str):
        """Return a boolean file is can ingest."""
        try:
            text_from_pdf = convert_pdf_to_text(path)
            txt_list = text_from_pdf.split('\n')
            result = []
            for text in txt_list:
                text_list = text.split(' - ')
                if len(text_list) == 1:
                    quote_model_instance = QuoteModel(body=text)
                else:
                    quote_model_instance = QuoteModel(body=text_list[0], author=text_list[1])
                result.append(quote_model_instance)
            return  result
        except Exception as ex:
            return []


def convert_pdf_to_text(pdf_path):
    """Return a text."""
    result = subprocess.run(["pdftotext", pdf_path], capture_output=True)

    text = result.stdout.decode("utf-8")
    return text