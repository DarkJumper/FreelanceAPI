import pytest

from freelanceapi.msr.MsrDict import MsrRecordDict
from freelanceapi.msr.MsrStr import MsrRecordStr
from .ExampleRows import exmaple_empty_row, example_msrrecord_row
from .ClassifyedExample import example_empty_data, example_classifyed_msrrecord


def test_KeyError_MsrRecordDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = MsrRecordDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_MsrRecordDict(example_msrrecord_row):
    with pytest.raises(KeyError):
        mod_list = MsrRecordDict()
        data = example_msrrecord_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_MsrRecordDict_prepare_merge(example_msrrecord_row, example_classifyed_msrrecord):
    mod_list = MsrRecordDict()
    mod_list.prepare_merge(example_msrrecord_row)
    assert mod_list.merge_dict() == example_classifyed_msrrecord


def test_KeyError_MsrRecordStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = MsrRecordStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_MsrRecordStr(example_classifyed_msrrecord):
    with pytest.raises(KeyError):
        mod_list = MsrRecordStr()
        data = example_classifyed_msrrecord
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_MsrRecordStr_prepare_merge(example_classifyed_msrrecord, example_msrrecord_row):
    mod_list = MsrRecordStr()
    mod_list.prepare_merge(example_classifyed_msrrecord)
    assert mod_list.merge_string() == example_msrrecord_row