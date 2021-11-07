import pytest

from freelanceapi.msr.MsrDict import GwyDict
from freelanceapi.msr.MsrStr import GwyStr
from .ExampleRows import exmaple_empty_row, example_gwy_row
from .ClassifyedExample import example_empty_data, example_classifyed_gwy


def test_KeyError_GwyDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = GwyDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_GwyDict(example_gwy_row):
    with pytest.raises(KeyError):
        mod_list = GwyDict()
        data = example_gwy_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_GwyDict_prepare_merge(example_gwy_row, example_classifyed_gwy):
    mod_list = GwyDict()
    mod_list.prepare_merge(example_gwy_row)
    assert mod_list.merge_dict() == example_classifyed_gwy


def test_KeyError_GwyStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = GwyStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_GwyStr(example_classifyed_gwy):
    with pytest.raises(KeyError):
        mod_list = GwyStr()
        data = example_classifyed_gwy
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_GwyStr_prepare_merge(example_classifyed_gwy, example_gwy_row):
    mod_list = GwyStr()
    mod_list.prepare_merge(example_classifyed_gwy)
    assert mod_list.merge_string() == example_gwy_row