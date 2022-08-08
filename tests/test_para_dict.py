import pytest
from freelanceapi.row_identificator import ParaData
from freelanceapi.sections.para_dict import ParaDataDict

from .ClassifyedExample import example_classifyed_paradata, example_empty_data
from .ExampleRows import example_paradata_row, exmaple_empty_row


def test_ParaDataDict_prepare_merge(example_paradata_row, example_classifyed_paradata):
    mod_list = ParaDataDict()
    assert mod_list.merge_dict(example_paradata_row.split(";")) == example_classifyed_paradata


def test_ParaDataString(example_paradata_row, example_classifyed_paradata):
    check = ParaData(**example_classifyed_paradata)
    assert check.string() == example_paradata_row
