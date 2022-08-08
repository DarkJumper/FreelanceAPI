import pytest
from freelanceapi.row_identificator import PbvOpjpath
from freelanceapi.sections.pbaum_dict import PbvObjpathDict

from .ClassifyedExample import (example_classifyed_pbvobjpath, example_empty_data)
from .ExampleRows import example_pbvobjpath_row, exmaple_empty_row


def test_PbvObjpathDict_prepare_merge(example_pbvobjpath_row, example_classifyed_pbvobjpath):
    mod_list = PbvObjpathDict()
    assert mod_list.merge_dict(example_pbvobjpath_row.split(";")) == example_classifyed_pbvobjpath


def test_PbvObjpathString(example_pbvobjpath_row, example_classifyed_pbvobjpath):
    check = PbvOpjpath(**example_classifyed_pbvobjpath)
    assert check.string() == example_pbvobjpath_row
