import pytest
from freelanceapi.sections.gwy_dict import GwyDict

from .ClassifyedExample import example_classifyed_gwy, example_empty_data
from .ExampleRows import example_gwy_row, exmaple_empty_row


def test_GwyDict_prepare_merge(example_gwy_row, example_classifyed_gwy):
    mod_list = GwyDict()
    assert mod_list.merge_dict(example_gwy_row.split(";")) == example_classifyed_gwy
