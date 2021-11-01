from .msr.KeyWord import KeyWord
from .msr.ParaData import ParaData
from .msr.MsrRecord import MsrRecord
from .msr.EamRecord import EamRecord
from .msr.UidAcc import UidAcc
from .msr.PbvObjpath import PbvObjpath
from .msr.MsrRef import MsrRef
from .msr.ParaRef import ParaRef
from .msr.Gwy import Gwy
from .utils.Exceptions import WrongeKey

EXPORTED_MSR_FACTORIES = {
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


def msr_row(listed_data: str, sep: str = ";") -> KeyWord:
    key_word, *_ = listed_data.split(sep)
    if key_word not in EXPORTED_MSR_FACTORIES.keys():
        raise WrongeKey(",".join(EXPORTED_MSR_FACTORIES.keys()), key_word, "The key is not defined for this function")
    base_class = EXPORTED_MSR_FACTORIES[key_word]
    base_class._first_execute(listed_data, sep=sep)
    return base_class
