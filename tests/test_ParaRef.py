import pytest
from freelanceapi.msr.MsrDict import ParaRefDict
from freelanceapi.msr.MsrStr import ParaRefStr

from .ClassifyedExample import example_classifyed_pararef, example_empty_data
from .ExampleRows import example_pararef_row, exmaple_empty_row


def test_KeyError_ParaRefDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = ParaRefDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_ParaRefDict(example_pararef_row):
    with pytest.raises(KeyError):
        mod_list = ParaRefDict()
        data = example_pararef_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_ParaRefDict_prepare_merge(example_pararef_row, example_classifyed_pararef):
    mod_list = ParaRefDict()
    mod_list.prepare_merge(example_pararef_row)
    assert mod_list.merge_dict() == example_classifyed_pararef


def test_KeyError_ParaRefStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = ParaRefStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_ParaRefStr(example_classifyed_pararef):
    with pytest.raises(KeyError):
        mod_list = ParaRefStr()
        data = example_classifyed_pararef
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_ParaRefStr_prepare_merge(example_classifyed_pararef, example_pararef_row):
    mod_list = ParaRefStr()
    mod_list.prepare_merge(example_classifyed_pararef)
    assert mod_list.merge_string() == example_pararef_row
