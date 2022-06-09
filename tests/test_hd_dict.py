import pytest
from freelanceapi.sections.hd_dict import MsrRefDict, ParaRefDict

from .ClassifyedExample import (example_classifyed_msrref, example_classifyed_pararef, example_empty_data)
from .ExampleRows import (example_msrref_row, example_pararef_row, exmaple_empty_row)


def test_ParaRefDict_prepare_merge(example_pararef_row, example_classifyed_pararef):
    mod_list = ParaRefDict()
    assert mod_list.merge_dict(example_pararef_row.split(";")) == example_classifyed_pararef


def test_MsrRefDict_prepare_merge(example_msrref_row, example_classifyed_msrref):
    mod_list = MsrRefDict()
    assert mod_list.merge_dict(example_msrref_row.split(";")) == example_classifyed_msrref
