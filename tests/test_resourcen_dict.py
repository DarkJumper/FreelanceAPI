import pytest
from freelanceapi.row_identificator import EamResourceassocation
from freelanceapi.sections.resourcen_dict import EamResourceDict

from .ClassifyedExample import example_classifyed_eamres, example_empty_data
from .ExampleRows import example_eamres_row, exmaple_empty_row


def test_EamResDict_prepare_merge(example_eamres_row, example_classifyed_eamres):
    mod_list = EamResourceDict()
    assert mod_list.merge_dict(example_eamres_row.split(";")) == example_classifyed_eamres


def test_EamResString(example_eamres_row, example_classifyed_eamres):
    check = EamResourceassocation(**example_classifyed_eamres)
    assert check.string() == example_eamres_row
