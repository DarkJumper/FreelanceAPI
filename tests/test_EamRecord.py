import pytest

from freelanceapi.EamRecord import EamRecord
from .ExampleRows import exmaple_empty_row, example_eamrecord_row
from .ClassifyedExample import example_empty_data, example_classifyed_eamrecord
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_EamRecord(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = EamRecord()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_EamRecord(example_eamrecord_row):
    with pytest.raises(WrongeKey):
        mod_list = EamRecord()
        data = example_eamrecord_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_EamRecord(example_eamrecord_row):
    mod_list = EamRecord()
    mod_list._first_execute(example_eamrecord_row)
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
    mod_list._first_execute(example_eamrecord_row)
    assert mod_list.get_string == example_eamrecord_row


def test_dict_to_string_EamRecord(example_classifyed_eamrecord, example_eamrecord_row):
    mod_list = EamRecord()
    mod_list.dict_to_string(example_classifyed_eamrecord)
    assert mod_list.get_string == example_eamrecord_row
    assert mod_list.get_dict == example_classifyed_eamrecord


def test_string_to_dict_EamRecord(example_classifyed_eamrecord, example_eamrecord_row):
    mod_list = EamRecord()
    mod_list.string_to_dict(example_eamrecord_row)
    assert mod_list.get_string == example_eamrecord_row
    assert mod_list.get_dict == example_classifyed_eamrecord


def test_string_to_dict_WrongeData_EamRecord(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = EamRecord()
        mod_list.string_to_dict(exmaple_empty_row)


def test_string_to_dict_WrongKey_EamRecord(example_eamrecord_row):
    with pytest.raises(WrongeKey):
        mod_list = EamRecord()
        data = example_eamrecord_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.string_to_dict(test)


def test_dict_to_string_WrongeData_EamRecord(example_empty_data):
    with pytest.raises(WrongeData):
        mod_list = EamRecord()
        mod_list.dict_to_string(example_empty_data)


def test_dict_to_string_WrongKey_EamRecord(example_classifyed_eamrecord):
    with pytest.raises(WrongeKey):
        mod_list = EamRecord()
        test = example_classifyed_eamrecord
        test['KW'] = "TEST"
        mod_list.dict_to_string(test)