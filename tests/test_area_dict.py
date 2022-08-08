import pytest
from freelanceapi.row_identificator import Area
from freelanceapi.sections.area_dict import AreaDict

from .ClassifyedExample import example_classifyed_area, example_empty_data
from .ExampleRows import example_area_row, exmaple_empty_row


def test_AreaDict_prepare_merge(example_area_row, example_classifyed_area):
    mod_list = AreaDict()
    assert mod_list.merge_dict(example_area_row.split(";")) == example_classifyed_area


def test_AreaString(example_area_row, example_classifyed_area):
    check = Area(**example_classifyed_area)
    assert check.string() == example_area_row
