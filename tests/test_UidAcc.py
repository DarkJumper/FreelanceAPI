import pytest

from freelanceapi.msr.UidAcc import UidAcc
from .ExampleRows import exmaple_empty_row, example_uidacc_row
from .ClassifyedExample import example_empty_data, example_classifyed_uidacc
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_UidAcc(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = UidAcc()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_UidAcc(example_uidacc_row):
    with pytest.raises(WrongeKey):
        mod_list = UidAcc()
        data = example_uidacc_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_UidAcc(example_uidacc_row):
    mod_list = UidAcc()
    mod_list._first_execute(example_uidacc_row)
    assert mod_list.get_dict == {
        'KW': '[UID:ACCMSR]',
        'LEN': '5',
        'USER1': {
            'USER': 'USER1',
            'ACC': '3'
            },
        'USER2': {
            'USER': 'USER2',
            'ACC': '3'
            },
        'GUEST': {
            'USER': 'GUEST',
            'ACC': '1'
            },
        'USER3': {
            'USER': 'USER3',
            'ACC': '1'
            },
        'USER4': {
            'USER': 'USER4',
            'ACC': '1'
            }
        }


def test_get_string_UidAcc(example_uidacc_row):
    mod_list = UidAcc()
    mod_list._first_execute(example_uidacc_row)
    assert mod_list.get_string == example_uidacc_row


def test_dict_to_string_UidAcc(example_classifyed_uidacc, example_uidacc_row):
    mod_list = UidAcc()
    mod_list.dict_to_string(example_classifyed_uidacc)
    assert mod_list.get_string == example_uidacc_row
    assert mod_list.get_dict == example_classifyed_uidacc


def test_string_to_dict_UidAcc(example_classifyed_uidacc, example_uidacc_row):
    mod_list = UidAcc()
    mod_list.string_to_dict(example_uidacc_row)
    assert mod_list.get_string == example_uidacc_row
    assert mod_list.get_dict == example_classifyed_uidacc


def test_string_to_dict_WrongeData_UidAcc(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = UidAcc()
        mod_list.string_to_dict(exmaple_empty_row)


def test_string_to_dict_WrongKey_UidAcc(example_uidacc_row):
    with pytest.raises(WrongeKey):
        mod_list = UidAcc()
        data = example_uidacc_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.string_to_dict(test)


def test_dict_to_string_WrongeData_UidAcc(example_empty_data):
    with pytest.raises(WrongeData):
        mod_list = UidAcc()
        mod_list.dict_to_string(example_empty_data)


def test_dict_to_string_WrongKey_UidAcc(example_classifyed_uidacc):
    with pytest.raises(WrongeKey):
        mod_list = UidAcc()
        test = example_classifyed_uidacc
        test['KW'] = "TEST"
        mod_list.dict_to_string(test)