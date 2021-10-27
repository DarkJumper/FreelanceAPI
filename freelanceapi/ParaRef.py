from typing import Dict

from .KeyWord import BaseClass


class ParaRef(BaseClass):
    keys: list[str] = ["KW", "VN", "DT", "?0", "PI", "END"]
    expected_key = "[LAD:PARA_REF]"