from .hwm.HwmDict import BeginIODescriptionDict, Hw2BlobDict, HwmDict
from .hwm.HwmStr import BeginIODescriptionStr, Hw2BlobStr, HwmStr
from .msr.MsrDict import (
    EamRecordDict, GwyDict, MsrDict, MsrRecordDict, MsrRefDict, ParaDataDict, ParaRefDict, PbvObjpathDict, UidAccDict
    )
from .msr.MsrStr import (
    EamRecordStr, GwyStr, MsrRecordStr, MsrRefStr, MsrStr, ParaDataStr, ParaRefStr, PbvObjpathStr, UidAccStr
    )
from .project.ProjectDict import AreaDict, PbNodeDict
from .project.ProjectStr import AreaStr, PbNodeStr


class ExportedFreelanceFactories:
    _msr_factories = {
        "[PARA:PARADATA]": (ParaDataDict, ParaDataStr),
        "[UID:ACCMSR]'": (UidAccDict, UidAccStr),
        "[GWY:ACCEAM]": (GwyDict, GwyStr),
        "[GWY:ACCMSR]": (GwyDict, GwyStr),
        "[MSR:RECORD]": (MsrRecordDict, MsrRecordStr),
        "[LAD:MSR_REF]": (MsrRefDict, MsrRefStr),
        "[LAD:PARA_REF]": (ParaRefDict, ParaRefStr),
        "[EAM:RECORD]": (EamRecordDict, EamRecordStr),
        "[PBV:OBJPATH]": (PbvObjpathDict, PbvObjpathStr),
        "[HW2_BLOB]": (Hw2BlobDict, Hw2BlobStr),
        "[PB:NODE]": (PbNodeDict, PbNodeStr),
        "[BEGIN_IODESCRIPTION]": (BeginIODescriptionDict, BeginIODescriptionStr),
        "[AREA]": (AreaDict, AreaStr)
        }

    def __getitem__(self, key):
        return self._msr_factories[key]

    def __repr__(self):
        return repr(self._msr_factories)

    def __len__(self):
        return len(self._msr_factories)

    def copy(self):
        return self._msr_factories.copy()

    def keys(self):
        return self._msr_factories.keys()

    def values(self):
        return self._msr_factories.values()
