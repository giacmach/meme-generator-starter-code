"""Build Ingestor.

is_file_compatible and is_file_compatible.
"""
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.PDFIngestor import PDFIngestor


class Ingestor:
    """Build DocxIngestor.

    is_file_compatible and parse.
    """

    @classmethod
    def is_file_compatible(cls, file_path):
        """Return ingestor by file type."""
        if file_path.endswith(('.pdf', '.csv', '.docx', '.txt')):
            return True

        return False

    @classmethod
    def parse(cls, path: str):
        """Return ingestor by file type."""
        cls_ingestor = get_ingestor_by_file_type(path)
        if cls_ingestor and cls_ingestor.can_ingest(path):
            return cls_ingestor.parse(path)

        return []


def get_ingestor_by_file_type(file_path):
    """Return ingestor by file type."""
    if file_path.endswith('.pdf'):
        return PDFIngestor()
    if file_path.endswith('.csv'):
        return CSVIngestor()
    if file_path.endswith('.docx'):
        return DocxIngestor()
    if file_path.endswith('.txt'):
        return TextIngestor()

    return None
