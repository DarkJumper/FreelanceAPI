from .KeyWord import KeyWord
from .ParaData import ParaData
from .MsrRecord import MsrRecord
from .EamRecord import EamRecord
from .UidAcc import UidAcc
from .PbvObjpath import PbvObjpath
from .ParaRef import ParaRef
from .ParaRef import ParaRef

FACTORIES = {
    "[PARA:PARADATA]": ParaData(),
    "[MSR:RECORD]": MsrRecord(),
    "[UID:ACCMSR]": UidAcc(),
    "[EAM:RECORD]": EamRecord(),
    "[PBV:OBJPATH]": PbvObjpath(),
    "[LAD:MSR_REF]": ParaRef(),
    "[LAD:PARA_REF]": ParaRef()
    }


def exported_row(listed_data: str, sep: str = ";") -> KeyWord:
    key_word, *_ = listed_data.split(";")
    specifed_class = FACTORIES[key_word]
    specifed_class.evaluate_list(listed_data.split(sep))
    return specifed_class
