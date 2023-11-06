"""Build IngestorInterface.

Ingest and parse.
"""
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Build IngestorInterface.

    Ingest and parse.
    """

    @abstractmethod
    def can_ingest(cls, path: str):
        """Return a boolean file is can ingest."""
        return True

    @abstractmethod
    def parse(cls, path: str):
        """Return a boolean file is can ingest."""
        pass
