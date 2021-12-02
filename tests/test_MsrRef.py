import pytest
from freelanceapi.msr.MsrDict import MsrRefDict
from freelanceapi.msr.MsrStr import MsrRefStr

from .ClassifyedExample import example_classifyed_msrref, example_empty_data
from .ExampleRows import example_msrref_row, exmaple_empty_row


def test_KeyError_MsrRefDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = MsrRefDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_MsrRefDict(example_msrref_row):
    with pytest.raises(KeyError):
        mod_list = MsrRefDict()
        data = example_msrref_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_MsrRefDict_prepare_merge(example_msrref_row, example_classifyed_msrref):
    mod_list = MsrRefDict()
    mod_list.prepare_merge(example_msrref_row)
    assert mod_list.merge_dict() == example_classifyed_msrref


def test_KeyError_MsrRefStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = MsrRefStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_MsrRefStr(example_classifyed_msrref):
    with pytest.raises(KeyError):
        mod_list = MsrRefStr()
        data = example_classifyed_msrref
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_MsrRefStr_prepare_merge(example_classifyed_msrref, example_msrref_row):
    mod_list = MsrRefStr()
    mod_list.prepare_merge(example_classifyed_msrref)
    assert mod_list.merge_string() == example_msrref_row
