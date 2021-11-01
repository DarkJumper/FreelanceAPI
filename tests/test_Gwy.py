import pytest

from freelanceapi.msr.Gwy import Gwy
from .ExampleRows import exmaple_empty_row, example_gwy_row
from .ClassifyedExample import example_empty_data, example_classifyed_gwy
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_Gwy(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = Gwy()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_Gwy(example_gwy_row):
    with pytest.raises(WrongeKey):
        mod_list = Gwy()
        data = example_gwy_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_Gwy(example_gwy_row):
    mod_list = Gwy()
    mod_list._first_execute(example_gwy_row)
    assert mod_list.get_dict == {
        'KW': '[GWY:ACCEAM]',
        'MN': '54321_AUF',
        'LEN': '1',
        'T164': {
            'GN': 'T164',
            'G1': '1',
            'G2': '1'
            },
        'O168': {
            'GN': 'O168',
            'G1': '3',
            'G2': '0'
            },
        'END': '1'
        }


def test_get_string_Gwy(example_gwy_row):
    mod_list = Gwy()
    mod_list._first_execute(example_gwy_row)
    assert mod_list.get_string == example_gwy_row


def test_dict_to_string_Gwy(example_classifyed_gwy, example_gwy_row):
    mod_list = Gwy()
    mod_list.dict_to_string(example_classifyed_gwy)
    assert mod_list.get_string == example_gwy_row
    assert mod_list.get_dict == example_classifyed_gwy


def test_string_to_dict_Gwy(example_classifyed_gwy, example_gwy_row):
    mod_list = Gwy()
    mod_list.string_to_dict(example_gwy_row)
    assert mod_list.get_string == example_gwy_row
    assert mod_list.get_dict == example_classifyed_gwy


def test_string_to_dict_WrongeData_Gwy(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = Gwy()
        mod_list.string_to_dict(exmaple_empty_row)


def test_string_to_dict_WrongKey_Gwy(example_gwy_row):
    with pytest.raises(WrongeKey):
        mod_list = Gwy()
        data = example_gwy_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.string_to_dict(test)


def test_dict_to_string_WrongeData_Gwy(example_empty_data):
    with pytest.raises(WrongeData):
        mod_list = Gwy()
        mod_list.dict_to_string(example_empty_data)


def test_dict_to_string_WrongKey_Gwy(example_classifyed_gwy):
    with pytest.raises(WrongeKey):
        mod_list = Gwy()
        test = example_classifyed_gwy
        test['KW'] = "TEST"
        mod_list.dict_to_string(test)