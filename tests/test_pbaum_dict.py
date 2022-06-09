import pytest
from freelanceapi.sections.pbaum_dict import PbvObjpathDict

from .ClassifyedExample import (example_classifyed_pbvobjpath, example_empty_data)
from .ExampleRows import example_pbvobjpath_row, exmaple_empty_row


def test_PbvObjpathDict_prepare_merge(example_pbvobjpath_row, example_classifyed_pbvobjpath):
    mod_list = PbvObjpathDict()
    assert mod_list.merge_dict(example_pbvobjpath_row.split(";")) == example_classifyed_pbvobjpath
