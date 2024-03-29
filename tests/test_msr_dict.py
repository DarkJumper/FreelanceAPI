import pytest
from freelanceapi.row_identificator import MsrRec, UidAcc
from freelanceapi.sections.msr_dict import MsrRecordDict, UidAccDict

from .ClassifyedExample import (example_classifyed_msrrecord, example_classifyed_uidacc)
from .ExampleRows import example_msrrecord_row, example_uidacc_row


def test_MsrRecordDict_prepare_merge(example_msrrecord_row, example_classifyed_msrrecord):
    mod_list = MsrRecordDict()
    assert mod_list.merge_dict(example_msrrecord_row.split(";")) == example_classifyed_msrrecord


def test_MsrRecordString(example_msrrecord_row, example_classifyed_msrrecord):
    check = MsrRec(**example_classifyed_msrrecord)
    assert check.string() == example_msrrecord_row


def test_UidAccDict_prepare_merge(example_uidacc_row, example_classifyed_uidacc):
    mod_list = UidAccDict()
    assert mod_list.merge_dict(example_uidacc_row.split(";")) == example_classifyed_uidacc


def test_UidAccString(example_uidacc_row, example_classifyed_uidacc):
    check = UidAcc(**example_classifyed_uidacc)
    assert check.string() == example_uidacc_row
