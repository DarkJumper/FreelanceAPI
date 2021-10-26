from typing import Dict
from collections import defaultdict

from .KeyWord import BaseClass


class ParaRef(BaseClass):
    classifyed_data: Dict = defaultdict(lambda: None)
    keys: list[str] = ["KW", "VN", "DT", "?0", "PI", "END"]
    expected_key = "[LAD:PARA_REF]"