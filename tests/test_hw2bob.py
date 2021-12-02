import pytest
from freelanceapi.hwm.HwmDict import Hw2BlobDict
from freelanceapi.hwm.HwmStr import Hw2BlobStr

from .ClassifyedExample import example_classifyed_hw2blob, example_empty_data
from .ExampleRows import exmaple_empty_row, exmaple_hw2blob_row


def test_KeyError_Hw2BlobDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = Hw2BlobDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_Hw2BlobDict(exmaple_hw2blob_row):
    with pytest.raises(KeyError):
        mod_list = Hw2BlobDict()
        data = exmaple_hw2blob_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_Hw2BlobDict_prepare_merge(exmaple_hw2blob_row, example_classifyed_hw2blob):
    mod_list = Hw2BlobDict()
    mod_list.prepare_merge(exmaple_hw2blob_row)
    assert mod_list.merge_dict() == example_classifyed_hw2blob


def test_KeyError_Hw2BlobStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = Hw2BlobStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_Hw2BlobStr(example_classifyed_hw2blob):
    with pytest.raises(KeyError):
        mod_list = Hw2BlobStr()
        data = example_classifyed_hw2blob
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_Hw2BlobStr_prepare_merge(example_classifyed_hw2blob, exmaple_hw2blob_row):
    mod_list = Hw2BlobStr()
    mod_list.prepare_merge(example_classifyed_hw2blob)
    assert mod_list.merge_string() == exmaple_hw2blob_row
