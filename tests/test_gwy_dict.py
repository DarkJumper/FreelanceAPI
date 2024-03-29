import pytest

from freelanceapi.row_identificator import GwyAccEam
from freelanceapi.sections.gwy_dict import GwyEamDict, GwyMsrDict

from .ClassifyedExample import example_classifyed_gwy, example_empty_data
from .ExampleRows import example_gwy_row, exmaple_empty_row


def test_GwyDict_prepare_merge(example_gwy_row, example_classifyed_gwy):
    mod_list = GwyEamDict()
    assert mod_list.merge_dict(example_gwy_row.split(";")) == example_classifyed_gwy


def test_GwyString(example_gwy_row, example_classifyed_gwy):
    check = GwyAccEam(**example_classifyed_gwy)
    assert check.string() == example_gwy_row
