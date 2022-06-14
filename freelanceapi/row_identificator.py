from abc import ABC, abstractmethod
from typing import Callable, Dict, Tuple, Union

from pydantic import BaseModel

from .sections.area_dict import AreaDict
from .sections.eam_dict import EamRecordDict
from .sections.gwy_dict import GwyDict
from .sections.hd_dict import MsrRefDict, ParaRefDict
from .sections.hw2_dict import BeginIODescriptionDict, Hw2BlobDict
from .sections.msr_dict import MsrRecordDict, UidAccDict
from .sections.node_dict import PbNodeDict
from .sections.para_dict import ParaDataDict
from .sections.pbaum_dict import PbvObjpathDict
from .sections.resourcen_dict import EamResourceDict


class RowIdentification(BaseModel, ABC):
    ID: str = None

    def string(self) -> str:
        """
        string creates a string with all propertys.

        Returns:
            str: returns a useable repesentation ot the property as a string.
        """
        all_values = list(self.dict().values())
        if None in all_values:
            raise AttributeError('Values arent assigent')
        return ';'.join(map(str, all_values))


# sourcery skip: remove-duplicate-dict-key
class MsrRec(RowIdentification):
    NA: int = None
    MN: str = None
    LB: str = None
    MT: str = None
    ST: str = None
    LT: str = None
    NI1: str = None
    AD: int = None
    SB: int = None
    NI2: str = None
    NI3: str = None
    NI4: str = None
    NI5: str = None


class UidAcc(RowIdentification):
    LEN: int = None
    test: list[Dict] = None


class ParaData(RowIdentification):
    pass


class PBNode(RowIdentification):
    pass


class EamRecord(RowIdentification):
    pass


class Area(RowIdentification):
    pass


class EamResourceassocation(RowIdentification):
    pass


class ParaRef(RowIdentification):
    pass


class MsrRef(RowIdentification):
    pass


class PbvOpjpath(RowIdentification):
    pass


class GwyAccEam(RowIdentification):
    pass


class GwyAccMsr(RowIdentification):
    pass


class Hw2Blob(RowIdentification):
    pass


class IoDescription(RowIdentification):
    pass


__FREELANCE_IDENTIFICATION = {
    "[MSR:RECORD]": (MsrRec, MsrRecordDict),
    "[UID:ACCMSR]": (UidAcc, UidAccDict),
    "[PARA:PARADATA]": (ParaData, ParaDataDict),
    "[PB:NODE]": (PBNode, PbNodeDict),
    "[EAM:RECORD]": (EamRecord, EamRecordDict),
    "[AREA]": (Area, AreaDict),
    "[EAM:RESOURCEASSOCIATION]": (EamResourceassocation, EamResourceDict),
    "[LAD:PARA_REF]": (ParaRef, ParaRefDict),
    "[LAD:MSR_REF]": (MsrRef, MsrRefDict),
    "[PBV:OBJPATH]": (PbvOpjpath, PbvObjpathDict),
    "[GWY:ACCEAM]": (GwyAccEam, GwyDict),
    "[GWY:ACCEAM]": (GwyAccMsr, GwyDict),
    "[HW2_BLOB]": (Hw2Blob, Hw2BlobDict),
    "[BEGIN_IODESCRIPTION]": (IoDescription, BeginIODescriptionDict)
    }


def row_identificator(row: tuple[str]) -> RowIdentification:
    if row[0] not in __FREELANCE_IDENTIFICATION.keys():
        raise AttributeError('cant find identificator!')
    (id, CreateDict) = __FREELANCE_IDENTIFICATION[row[0]]
    row_dict = CreateDict().merge_dict(row)
    return id(**row_dict)
