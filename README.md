# FreecomAPI

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PyPI version](https://badge.fury.io/py/freelanceapi.svg)](https://badge.fury.io/py/freelanceapi)
[![GitHub license](https://img.shields.io/github/license/DarkJumper/FreelanceAPI)](https://github.com/DarkJumper/FreelanceAPI/blob/main/LICENSE)

With the Freelance API an export file from the ABB Freelance control system can be evaluated.


## Functions:

ContextManger:
- read_export_file: For now it can only evaluate the CSV export file
- get_sections: All ranges from the csv file can be output directly.

This is how it is done:

```
from freelanceapi import get_sections, read_export_file
from freelanceapi.sections import HW2


with read_export_file("freelance_export_csv.csv", "csv") as file:
    section_data = get_sections(file, section=HW2) 
    print(section_data)
    output =>......
```

In this example, the complete range of field IO is output.

The following sections can be read out:
- ProjectComment:
- AreaDefinition:
- ProjectHeader:
- ResourceAssociation:
- HardWareManager:
- HW2:
- OPCConn:
- Conn:
- HDTextList:
- HD:
- MSR:
- OPCAdress:
- EAMInit:
- EAM:
- Node:
- Pbaum:

## It provides:

Meanings of the Dict Keys:
- KW: Key Word
- LEN: Length of Dataset
- NA: Next element available
- MN: Measuring point name
- MT: Module Type
- ST: Short Text
- LT: Long Text
- AD: Area Definition
- SB: Status Bit
- VN: Variable Name
- DT: Data Typ
- VT: Variable Text
- PI: Process image
- EX: Exported Variable
- VC: Variable(0) or Const (1)
- FB: FBS Name
- LB: Libary
- DTMN: DTM Number
- DTMC: DTM Config
- QC: Quantity counter
- FN: Function Name
- CN: Channel Name
- IO: Input or Output
- UB: Used Byte
- B: Bit
- BL: Byte Length
- C: Commend
- AC: Area Char
- LA: Length of Area Text
- AN: Area Name

## :warning: Developer Info

All keys that contain a ? cannot be assigned to a function.

