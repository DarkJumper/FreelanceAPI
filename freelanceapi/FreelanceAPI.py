from .KeyWord import KeyWord
from .ParaData import ParaData
from .MsrRecord import MsrRecord
from .EamRecord import EamRecord
from .UidAcc import UidAcc
from .PbvObjpath import PbvObjpath
from .MsrRef import MsrRef
from .ParaRef import ParaRef
from .Gwy import Gwy

EXPORTED_FACTORIES = {
    "[PARA:PARADATA]": ParaData(),
    "[MSR:RECORD]": MsrRecord(),
    "[UID:ACCMSR]": UidAcc(),
    "[EAM:RECORD]": EamRecord(),
    "[PBV:OBJPATH]": PbvObjpath(),
    "[LAD:MSR_REF]": MsrRef(),
    "[LAD:PARA_REF]": ParaRef(),
    "[GWY:ACCEAM]": Gwy(),
    "[GWY:ACCMSR]": Gwy()
    }


def exported_row(listed_data: str, sep: str = ";") -> KeyWord:
    key_word, *_ = listed_data.split(sep)
    base_class = EXPORTED_FACTORIES[key_word]
    base_class._first_execute(listed_data, sep=sep)
    return base_class
