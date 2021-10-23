import pytest

from freelanceapi.UidAcc import UidAcc
from .ExampleRows import exmaple_empty_row, example_uidacc_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_UidAcc(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = UidAcc()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_UidAcc(example_uidacc_row):
    with pytest.raises(WrongeKey):
        mod_list = UidAcc()
        data = example_uidacc_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_UidAcc(example_uidacc_row):
    mod_list = UidAcc()
    data = example_uidacc_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {
        'USER1': ['USER1', '3'],
        'USER2': ['USER2', '3'],
        'GUEST': ['GUEST', '1'],
        'USER3': ['USER3', '1'],
        'USER4': ['USER4', '1']
        }


def test_get_string_UidAcc(example_uidacc_row):
    mod_list = UidAcc()
    data = example_uidacc_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_uidacc_row


def test_modify_UidAcc(example_uidacc_row):
    mod_list = UidAcc()
    data = example_uidacc_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"USER1": "1"})
    assert mod_list.get_dict == {
        'USER1': ['USER1', '1'],
        'USER2': ['USER2', '3'],
        'GUEST': ['GUEST', '1'],
        'USER3': ['USER3', '1'],
        'USER4': ['USER4', '1']
        }
    assert mod_list.get_string == "[UID:ACCMSR];5;USER1;1;USER2;3;GUEST;1;USER3;1;USER4;1"