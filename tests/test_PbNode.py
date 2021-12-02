import pytest
from freelanceapi.project.ProjectDict import PbNodeDict
from freelanceapi.project.ProjectStr import PbNodeStr

from .ClassifyedExample import example_classifyed_pbnode, example_empty_data
from .ExampleRows import exmaple_empty_row, exmaple_pbnode_row


def test_KeyError_PbNodeDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = PbNodeDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_PbNodeDict(exmaple_pbnode_row):
    with pytest.raises(KeyError):
        mod_list = PbNodeDict()
        data = exmaple_pbnode_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_PbNodeDict_prepare_merge(exmaple_pbnode_row, example_classifyed_pbnode):
    mod_list = PbNodeDict()
    mod_list.prepare_merge(exmaple_pbnode_row)
    assert mod_list.merge_dict() == example_classifyed_pbnode


def test_KeyError_PbNodeStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = PbNodeStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_PbNodeStr(example_classifyed_pbnode):
    with pytest.raises(KeyError):
        mod_list = PbNodeStr()
        data = example_classifyed_pbnode
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_PbNodeStr_prepare_merge(example_classifyed_pbnode, exmaple_pbnode_row):
    mod_list = PbNodeStr()
    mod_list.prepare_merge(example_classifyed_pbnode)
    assert mod_list.merge_string() == exmaple_pbnode_row
