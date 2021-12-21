import pytest
from freelanceapi.project.ProjectDict import AreaDict
from freelanceapi.project.ProjectStr import AreaStr

from .ClassifyedExample import example_classifyed_area, example_empty_data
from .ExampleRows import example_area_row, exmaple_empty_row


def test_KeyError_AreaDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = AreaDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_AreaDict(example_area_row):
    with pytest.raises(KeyError):
        mod_list = AreaDict()
        data = example_area_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_AreaDict_prepare_merge(example_area_row, example_classifyed_area):
    mod_list = AreaDict()
    mod_list.prepare_merge(example_area_row)
    assert mod_list.merge_dict() == example_classifyed_area


def test_KeyError_AreaStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = AreaStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_AreaStr(example_classifyed_area):
    with pytest.raises(KeyError):
        mod_list = AreaStr()
        data = example_classifyed_area
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_AreaStr_prepare_merge(example_classifyed_area, example_area_row):
    mod_list = AreaStr()
    mod_list.prepare_merge(example_classifyed_area)
    assert mod_list.merge_string() == example_area_row
