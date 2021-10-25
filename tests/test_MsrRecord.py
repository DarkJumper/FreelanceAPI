import pytest

from freelanceapi.MsrRecord import MsrRecord
from .ExampleRows import exmaple_empty_row, example_msrrecord_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_MsrRecord(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = MsrRecord()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_MsrRecord(example_msrrecord_row):
    with pytest.raises(WrongeKey):
        mod_list = MsrRecord()
        data = example_msrrecord_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_MsrRecord(example_msrrecord_row):
    mod_list = MsrRecord()
    data = example_msrrecord_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {
        'KW': '[MSR:RECORD]',
        'LEN': '1',
        'MN': 'M1234',
        'LIB': 'BST_LIB_MSR',
        'BT': 'M_BIN',
        'KT': 'kurztext',
        'LT': 'Langtext',
        '?0': '',
        'PA': '128',
        'ST': '1',
        '?1': '',
        '?2': '',
        '?3': '',
        'END': '2'
        }


def test_get_string_MsrRecord(example_msrrecord_row):
    mod_list = MsrRecord()
    data = example_msrrecord_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_msrrecord_row


def test_modify_MsrRecord(example_msrrecord_row):
    mod_list = MsrRecord()
    data = example_msrrecord_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"MN": "TEST"})
    assert mod_list.get_dict == {
        'KW': '[MSR:RECORD]',
        'LEN': '1',
        'MN': 'TEST',
        'LIB': 'BST_LIB_MSR',
        'BT': 'M_BIN',
        'KT': 'kurztext',
        'LT': 'Langtext',
        '?0': '',
        'PA': '128',
        'ST': '1',
        '?1': '',
        '?2': '',
        '?3': '',
        'END': '2'
        }
    assert mod_list.get_string == "[MSR:RECORD];1;TEST;BST_LIB_MSR;M_BIN;kurztext;Langtext;;128;1;;;;2"