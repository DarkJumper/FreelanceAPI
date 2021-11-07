import pytest

from freelanceapi.msr.MsrDict import EamRecordDict
from freelanceapi.msr.MsrStr import EamRecordStr
from .ExampleRows import exmaple_empty_row, example_eamrecord_row
from .ClassifyedExample import example_empty_data, example_classifyed_eamrecord


def test_KeyError_EamRecordDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = EamRecordDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_EamRecordDict(example_eamrecord_row):
    with pytest.raises(KeyError):
        mod_list = EamRecordDict()
        data = example_eamrecord_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_EamRecordDict_prepare_merge(example_eamrecord_row, example_classifyed_eamrecord):
    mod_list = EamRecordDict()
    mod_list.prepare_merge(example_eamrecord_row)
    assert mod_list.merge_dict() == example_classifyed_eamrecord


def test_KeyError_EamRecordStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = EamRecordStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_EamRecordStr(example_classifyed_eamrecord):
    with pytest.raises(KeyError):
        mod_list = EamRecordStr()
        data = example_classifyed_eamrecord
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_EamRecordStr_prepare_merge(example_classifyed_eamrecord, example_eamrecord_row):
    mod_list = EamRecordStr()
    mod_list.prepare_merge(example_classifyed_eamrecord)
    assert mod_list.merge_string() == example_eamrecord_row