from typing import Dict

from .KeyWord import BaseClass


class PbvObjpath(BaseClass):
    classifyed_data: Dict = dict()
    keys: list[str] = ["KW", "LEN", "LB", "FN"]
    expected_key = "[PBV:OBJPATH]"