from typing import Dict
from collections import defaultdict

from .KeyWord import BaseClass


class EamRecord(BaseClass):
    classifyed_data: Dict = defaultdict(lambda: None)
    keys: list[str] = ["KW", "LEN", "VN", "?0", "DT", "VT", "PI", 'EX']
    expected_key: str = "[EAM:RECORD]"
