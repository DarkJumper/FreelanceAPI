import pytest
from freelanceapi.row_identificator import MsrRef, ParaRef
from freelanceapi.sections.hd_dict import MsrRefDict, ParaRefDict

from .ClassifyedExample import (example_classifyed_msrref, example_classifyed_pararef, example_empty_data)
from .ExampleRows import (example_msrref_row, example_pararef_row, exmaple_empty_row)


def test_ParaRefDict_prepare_merge(example_pararef_row, example_classifyed_pararef):
    mod_list = ParaRefDict()
    assert mod_list.merge_dict(example_pararef_row.split(";")) == example_classifyed_pararef


def test_ParaRefString(example_pararef_row, example_classifyed_pararef):
    check = ParaRef(**example_classifyed_pararef)
    assert check.string() == example_pararef_row


def test_MsrRefDict_prepare_merge(example_msrref_row, example_classifyed_msrref):
    mod_list = MsrRefDict()
    assert mod_list.merge_dict(example_msrref_row.split(";")) == example_classifyed_msrref


def test_MsrRefString(example_msrref_row, example_classifyed_msrref):
    check = MsrRef(**example_classifyed_msrref)
    assert check.string() == example_msrref_row
