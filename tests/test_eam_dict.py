import pytest
from freelanceapi.row_identificator import EamRecord
from freelanceapi.sections.eam_dict import EamRecordDict

from .ClassifyedExample import example_classifyed_eamrecord, example_empty_data
from .ExampleRows import example_eamrecord_row, exmaple_empty_row


def test_EamRecordDict_prepare_merge(example_eamrecord_row, example_classifyed_eamrecord):
    mod_list = EamRecordDict()
    assert mod_list.merge_dict(example_eamrecord_row.split(";")) == example_classifyed_eamrecord


def test_EamRecordString(example_eamrecord_row, example_classifyed_eamrecord):
    check = EamRecord(**example_classifyed_eamrecord)
    assert check.string() == example_eamrecord_row
