from KeyWord import KeyWord
from ParaData import ParaData
from MsrRecord import MsrRecord
from collections import defaultdict
#from Gwy import Gwy

FACTORIES = {"[PARA:PARADATA]": ParaData(), "[MSR:RECORD]": MsrRecord()}


def exported_row(listed_data: str, sep: str = ";") -> KeyWord:
    key_word, *_ = listed_data.split(";")
    specifed_class = FACTORIES[key_word]
    specifed_class.evaluate_list(listed_data.split(sep))
    return specifed_class
