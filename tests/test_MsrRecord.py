import pytest

from freelanceapi.msr.MsrRecord import MsrRecord
from .ExampleRows import exmaple_empty_row, example_msrrecord_row
from .ClassifyedExample import example_empty_data, example_classifyed_msrrecord
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_MsrRecord(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = MsrRecord()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_MsrRecord(example_msrrecord_row):
    with pytest.raises(WrongeKey):
        mod_list = MsrRecord()
        data = example_msrrecord_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_MsrRecord(example_msrrecord_row):
    mod_list = MsrRecord()
    mod_list._first_execute(example_msrrecord_row)
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
    mod_list._first_execute(example_msrrecord_row)
    assert mod_list.get_string == example_msrrecord_row


def test_dict_to_string_MsrRecord(example_classifyed_msrrecord, example_msrrecord_row):
    mod_list = MsrRecord()
    mod_list.dict_to_string(example_classifyed_msrrecord)
    assert mod_list.get_string == example_msrrecord_row
    assert mod_list.get_dict == example_classifyed_msrrecord


def test_string_to_dict_MsrRecord(example_classifyed_msrrecord, example_msrrecord_row):
    mod_list = MsrRecord()
    mod_list.string_to_dict(example_msrrecord_row)
    assert mod_list.get_string == example_msrrecord_row
    assert mod_list.get_dict == example_classifyed_msrrecord


def test_string_to_dict_WrongeData_MsrRecord(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = MsrRecord()
        mod_list.string_to_dict(exmaple_empty_row)


def test_string_to_dict_WrongKey_MsrRecord(example_msrrecord_row):
    with pytest.raises(WrongeKey):
        mod_list = MsrRecord()
        data = example_msrrecord_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.string_to_dict(test)


def test_dict_to_string_WrongeData_MsrRecord(example_empty_data):
    with pytest.raises(WrongeData):
        mod_list = MsrRecord()
        mod_list.dict_to_string(example_empty_data)


def test_dict_to_string_WrongKey_MsrRecord(example_classifyed_msrrecord):
    with pytest.raises(WrongeKey):
        mod_list = MsrRecord()
        test = example_classifyed_msrrecord
        test['KW'] = "TEST"
        mod_list.dict_to_string(test)