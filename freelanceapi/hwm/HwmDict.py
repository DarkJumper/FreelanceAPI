from typing import Dict, Protocol

from .HwmMetaData import HwmMetaData


class HwmDict(Protocol):
    """Basic representation of Msr rows as Dict."""

    def prepare_merge(self, dataset: str, sep=""):
        """Shares data needed for merging. """

    def merge_dict(self) -> Dict:
        """Merge data for Dataprocessing."""