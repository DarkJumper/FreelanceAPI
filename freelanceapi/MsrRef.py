from typing import Dict
from collections import defaultdict

from .KeyWord import BaseClass


class MsrRef(BaseClass):
    classifyed_data: Dict = defaultdict(lambda: None)
    keys: list[str] = ["KW", "MN"]
    expected_key = "[LAD:MSR_REF]"