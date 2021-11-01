from typing import Dict

from .KeyWord import BaseClass


class MsrRef(BaseClass):
    keys: list[str] = ["KW", "MN"]
    expected_key = "[LAD:MSR_REF]"