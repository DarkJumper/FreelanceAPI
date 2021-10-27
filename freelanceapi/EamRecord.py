from typing import Dict

from .KeyWord import BaseClass


class EamRecord(BaseClass):
    classifyed_data: Dict = dict()
    keys: list[str] = ["KW", "LEN", "VN", "?0", "DT", "VT", "PI", 'EX']
    expected_key: str = "[EAM:RECORD]"
