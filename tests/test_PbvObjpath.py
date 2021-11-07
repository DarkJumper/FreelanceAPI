import pytest

from freelanceapi.msr.MsrDict import PbvObjpathDict
from freelanceapi.msr.MsrStr import PbvObjpathStr
from .ExampleRows import exmaple_empty_row, example_pbvobjpath_row
from .ClassifyedExample import example_empty_data, example_classifyed_pbvobjpath


def test_KeyError_PbvObjpathDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = PbvObjpathDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_PbvObjpathDict(example_pbvobjpath_row):
    with pytest.raises(KeyError):
        mod_list = PbvObjpathDict()
        data = example_pbvobjpath_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_PbvObjpathDict_prepare_merge(example_pbvobjpath_row, example_classifyed_pbvobjpath):
    mod_list = PbvObjpathDict()
    mod_list.prepare_merge(example_pbvobjpath_row)
    assert mod_list.merge_dict() == example_classifyed_pbvobjpath


def test_KeyError_PbvObjpathStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = PbvObjpathStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_PbvObjpathStr(example_classifyed_pbvobjpath):
    with pytest.raises(KeyError):
        mod_list = PbvObjpathStr()
        data = example_classifyed_pbvobjpath
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_PbvObjpathStr_prepare_merge(example_classifyed_pbvobjpath, example_pbvobjpath_row):
    mod_list = PbvObjpathStr()
    mod_list.prepare_merge(example_classifyed_pbvobjpath)
    assert mod_list.merge_string() == example_pbvobjpath_row