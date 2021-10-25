from typing import Dict
from collections import defaultdict

from .KeyWord import BaseClass


class PbvObjpath(BaseClass):
    classifyed_data: Dict = defaultdict(lambda: None)
    keys: list[str] = ["KW", "LEN", "LB", "FN"]
    expected_key = "[PBV:OBJPATH]"