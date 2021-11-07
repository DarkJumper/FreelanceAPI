import pytest

from freelanceapi.msr.MsrDict import UidAccDict
from freelanceapi.msr.MsrStr import UidAccStr
from .ExampleRows import exmaple_empty_row, example_uidacc_row
from .ClassifyedExample import example_empty_data, example_classifyed_uidacc


def test_KeyError_UidAccDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = UidAccDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_UidAccDict(example_uidacc_row):
    with pytest.raises(KeyError):
        mod_list = UidAccDict()
        data = example_uidacc_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_UidAccDict_prepare_merge(example_uidacc_row, example_classifyed_uidacc):
    mod_list = UidAccDict()
    mod_list.prepare_merge(example_uidacc_row)
    assert mod_list.merge_dict() == example_classifyed_uidacc


def test_KeyError_UidAccStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = UidAccStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_UidAccStr(example_classifyed_uidacc):
    with pytest.raises(KeyError):
        mod_list = UidAccStr()
        data = example_classifyed_uidacc
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_UidAccStr_prepare_merge(example_classifyed_uidacc, example_uidacc_row):
    mod_list = UidAccStr()
    mod_list.prepare_merge(example_classifyed_uidacc)
    assert mod_list.merge_string() == example_uidacc_row