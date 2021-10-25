import pytest

from freelanceapi.EamRecord import EamRecord
from .ExampleRows import exmaple_empty_row, example_eamrecord_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_MsrRecord(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = EamRecord()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_EamRecord(example_eamrecord_row):
    with pytest.raises(WrongeKey):
        mod_list = EamRecord()
        data = example_eamrecord_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_EamRecord(example_eamrecord_row):
    mod_list = EamRecord()
    data = example_eamrecord_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {
        'KW': '[EAM:RECORD]',
        'LEN': '1',
        'VN': '54321_IN1',
        '?0': '0',
        'DT': 'INT',
        'VT': 'Variabel',
        'PI': '1',
        'EX': '0'
        }


def test_get_string_EamRecord(example_eamrecord_row):
    mod_list = EamRecord()
    data = example_eamrecord_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_eamrecord_row


def test_modify_EamRecord(example_eamrecord_row):
    mod_list = EamRecord()
    data = example_eamrecord_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"VN": "54321"})
    assert mod_list.get_dict == {
        'KW': '[EAM:RECORD]',
        'LEN': '1',
        'VN': '54321',
        '?0': '0',
        'DT': 'INT',
        'VT': 'Variabel',
        'PI': '1',
        'EX': '0'
        }
    assert mod_list.get_string == "[EAM:RECORD];1;54321;0;INT;Variabel;1;0"