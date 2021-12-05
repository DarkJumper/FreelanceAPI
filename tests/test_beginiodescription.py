import pytest
from freelanceapi.hwm.HwmDict import BeginIODescriptionDict
from freelanceapi.hwm.HwmStr import BeginIODescriptionStr

from .ClassifyedExample import (example_classifyed_beginiodescritpion, example_empty_data)
from .ExampleRows import example_beginiodescription_row, exmaple_empty_row


def test_KeyError_BeginIODescriptionDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = BeginIODescriptionDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_BeginIODescriptionDict(example_beginiodescription_row):
    with pytest.raises(KeyError):
        mod_list = BeginIODescriptionDict()
        data = example_beginiodescription_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_BeginIODescriptionDict_prepare_merge(example_beginiodescription_row, example_classifyed_beginiodescritpion):
    mod_list = BeginIODescriptionDict()
    mod_list.prepare_merge(example_beginiodescription_row)
    assert mod_list.merge_dict() == example_classifyed_beginiodescritpion


def test_KeyError_BeginIODescriptionStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = BeginIODescriptionStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_BeginIODescriptionStr(example_classifyed_beginiodescritpion):
    with pytest.raises(KeyError):
        mod_list = BeginIODescriptionStr()
        data = example_classifyed_beginiodescritpion
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_BeginIODescriptionStr_prepare_merge(example_classifyed_beginiodescritpion, example_beginiodescription_row):
    mod_list = BeginIODescriptionStr()
    mod_list.prepare_merge(example_classifyed_beginiodescritpion)
    assert mod_list.merge_string() == example_beginiodescription_row
