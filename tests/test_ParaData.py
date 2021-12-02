import pytest
from freelanceapi.msr.MsrDict import ParaDataDict
from freelanceapi.msr.MsrStr import ParaDataStr

from .ClassifyedExample import example_classifyed_paradata, example_empty_data
from .ExampleRows import example_paradata_row, exmaple_empty_row


def test_KeyError_ParaDataDict_Empty(exmaple_empty_row):
    with pytest.raises(KeyError):
        mod_list = ParaDataDict()
        mod_list.prepare_merge(exmaple_empty_row)


def test_KeyError_ParaDataDict(example_paradata_row):
    with pytest.raises(KeyError):
        mod_list = ParaDataDict()
        data = example_paradata_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.prepare_merge(test)


def test_ParaDataDict_prepare_merge(example_paradata_row, example_classifyed_paradata):
    mod_list = ParaDataDict()
    mod_list.prepare_merge(example_paradata_row)
    assert mod_list.merge_dict() == example_classifyed_paradata


def test_KeyError_ParaDataStr_Empty(example_empty_data):
    with pytest.raises(KeyError):
        mod_list = ParaDataStr()
        mod_list.prepare_merge(example_empty_data)


def test_KeyError_ParaDataStr(example_classifyed_paradata):
    with pytest.raises(KeyError):
        mod_list = ParaDataStr()
        data = example_classifyed_paradata
        data["KW"] = "TEST"
        mod_list.prepare_merge(data)


def test_ParaDataStr_prepare_merge(example_classifyed_paradata, example_paradata_row):
    mod_list = ParaDataStr()
    mod_list.prepare_merge(example_classifyed_paradata)
    assert mod_list.merge_string() == example_paradata_row
