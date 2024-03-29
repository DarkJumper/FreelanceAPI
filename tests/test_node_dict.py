import pytest
from freelanceapi.row_identificator import PBNode
from freelanceapi.sections.node_dict import PbNodeDict

from .ClassifyedExample import example_classifyed_pbnode, example_empty_data
from .ExampleRows import exmaple_empty_row, exmaple_pbnode_row


def test_PbNodeDict_prepare_merge(exmaple_pbnode_row, example_classifyed_pbnode):
    mod_list = PbNodeDict()
    assert mod_list.merge_dict(exmaple_pbnode_row.split(";")) == example_classifyed_pbnode


def test_PbNodeString(exmaple_pbnode_row, example_classifyed_pbnode):
    check = PBNode(**example_classifyed_pbnode)
    assert check.string() == exmaple_pbnode_row
