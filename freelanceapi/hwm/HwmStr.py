from typing import Protocol

from .HwmMetaData import HwmMetaData


class HwmStr(Protocol):
    """Basic representation of Msr rows as String"""

    def prepare_merge(self, dataset: str, sep=""):
        """Shares data needed for merging. """

    def merge_string(self) -> str:
        """Merge data for Dataprocessing."""