from typing import Dict

from .KeyWord import BaseClass


class MsrRecord(BaseClass):
    keys: list[str] = ["KW", "LEN", "MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    expected_key = "[MSR:RECORD]"
