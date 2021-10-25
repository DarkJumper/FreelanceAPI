from typing import Dict
from collections import defaultdict

from .KeyWord import BaseClass


class MsrRecord(BaseClass):
    classifyed_data: Dict = defaultdict(lambda: None)
    keys: list[str] = ["KW", "LEN", "MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    expected_key = "[MSR:RECORD]"
