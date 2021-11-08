from .msr.MsrDict import EamRecordDict, MsrDict, MsrRecordDict, MsrRefDict, ParaDataDict, ParaRefDict, PbvObjpathDict, UidAccDict, GwyDict
from .msr.MsrStr import EamRecordStr, MsrStr, MsrRecordStr, MsrRefStr, ParaDataStr, ParaRefStr, PbvObjpathStr, UidAccStr, GwyStr
from .hwm.HwmDict import HwmDict
from .hwm.HwmStr import HwmStr

EXPORTED_MSR_FACTORIES = {
    "[PARA:PARADATA]": (ParaDataDict, ParaDataStr),
    "[UID:ACCMSR]'": (UidAccDict, UidAccStr),
    "[GWY:ACCEAM]": (GwyDict, GwyStr),
    "[GWY:ACCMSR]": (GwyDict, GwyStr),
    "[MSR:RECORD]": (MsrRecordDict, MsrRecordStr),
    "[LAD:MSR_REF]": (MsrRefDict, MsrRefStr),
    "[LAD:PARA_REF]": (ParaRefDict, ParaRefStr),
    "[EAM:RECORD]": (EamRecordDict, EamRecordStr),
    "[PBV:OBJPATH]": (PbvObjpathDict, PbvObjpathStr)
    }

EXPORTED_HWM_FACTORIES = {}


def read_msr_row(listed_data: str, sep: str = ";") -> tuple[MsrDict, MsrStr]:
    """
    read_msr_row Matching instances to the key word are searched for and returned accordingly.

    Args:
        listed_data (str): An exported row of freelance is required. These must contain a key word. Key words are predefined.
        sep (str, optional): Seperator for the string must be set. Defaults to ";".

    Returns:
        tuple[MsrDict, MsrStr]: a tuple with an instance to convert to a dict and to convert to string
    """
    key_word, *_ = listed_data.split(sep)
    try:
        (dict_class, string_class) = EXPORTED_MSR_FACTORIES[key_word]
        return (dict_class(), string_class())
    except KeyError:
        print(f"unknown keyword in line: {key_word}.")


def read_hwm_row(listed_data: str, sep: str = ";") -> tuple[HwmDict, HwmStr]:
    """
    read_hwm_row Matching instances to the key word are searched for and returned accordingly.

    Args:
        listed_data (str): An exported row of freelance is required. These must contain a key word. Key words are predefined.
        sep (str, optional): Seperator for the string must be set. Defaults to ";".

    Returns:
        tuple[HwmDict, HwmStr]: a tuple with an instance to convert to a dict and to convert to string
    """
    key_word, *_ = listed_data.split(sep)
    try:
        (dict_class, string_class) = EXPORTED_HWM_FACTORIES[key_word]
        return (dict_class(), string_class())
    except KeyError:
        print(f"unknown keyword in line: {key_word}.")
