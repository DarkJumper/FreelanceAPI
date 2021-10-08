import pytest

from freelanceapi.utils.Modify import Modify, modify_dict_with_list_of_values, modify_dict_value
from freelanceapi.utils.Exceptions import KeyNotFoundError
from .ClassifyedExample import example_classifyed_paradata, example_classifyed_msrrecord, example_empty_data


def test_KeyNotFoundError_modify_dict_with_list_of_values(example_empty_data):
    with pytest.raises(KeyNotFoundError):
        mod_list = Modify(example_empty_data, {"Bt": "TEST"})
        assert mod_list.modify(modify_dict_with_list_of_values()) == {}


def test_modify_dict_with_list_of_values(example_classifyed_paradata):
    mod_list = Modify(example_classifyed_paradata, {"Bt0": "TEST"})
    assert mod_list.modify(modify_dict_with_list_of_values()) == {
        'OScan': ['OScan', '5', 'CHECK', '1', 'j'],
        'Bt0': ['Bt0', '5', 'MTEXT', '4', 'TEST'],
        'Bt1': ['Bt1', '5', 'MTEXT', '6', 'BEREIT'],
        'Mon': ['Mon', '5', 'CHECK', '1', 'j'],
        'Mp': ['Mp', '5', 'MPRIO', '1', '2'],
        'Mt': ['Mt', '5', 'MTEXT', '6', 'BEREIT'],
        'Wav1': ['Wav1', '5', 'HTEXT', '0', ''],
        'Gt': ['Gt', '13', 'CUSTSELLIST_2', '1', '0'],
        'Ast': ['Ast', '5', 'ASTAT', '0', ''],
        'Ht1': ['Ht1', '5', 'HTEXT', '0', ''],
        'Bz': ['Bz', '3', 'BZO', '0', ''],
        'BEDSEL': ['BEDSEL', '5', 'CHECK', '0', ''],
        'ChgShw': ['ChgShw', '5', 'CHECK', '0', ''],
        'Alex0': ['Alex0', '5', 'CHECK', '0', ''],
        'Alq0': ['Alq0', '5', 'CHECK', '0', ''],
        'Alex1': ['Alex1', '5', 'CHECK', '0', ''],
        'Alq1': ['Alq1', '5', 'CHECK', '0', ''],
        'Lmz': ['Lmz', '5', 'CHECK', '0', ''],
        'Aval': ['Aval', '5', 'CHECK', '0', ''],
        'Init': ['Init', '5', 'CHECK', '0', ''],
        'Acnt': ['Acnt', '4', 'WORD', '0', ''],
        'Align': ['Align', '4', 'WORD', '0', ''],
        'ATt1': ['ATt1', '7', 'DMSTIME', '0', ''],
        'ITt1': ['ITt1', '7', 'DMSTIME', '0', ''],
        'CAst1': ['CAst1', '4', 'BYTE', '0', ''],
        'OAst1': ['OAst1', '4', 'BYTE', '0', ''],
        'Nlst1': ['Nlst1', '4', 'BYTE', '0', ''],
        'Align1': ['Align1', '4', 'BYTE', '0', '']
        }
    assert mod_list.modify(modify_dict_with_list_of_values())["Bt0"] == ['Bt0', '5', 'MTEXT', '4', 'TEST']


def test_KeyNotFoundError_modify_dict_value(example_empty_data):
    with pytest.raises(KeyNotFoundError):
        mod_list = Modify(example_empty_data, {"M": "TEST"})
        assert mod_list.modify(modify_dict_value()) == {}


def test_modify_dict_value(example_classifyed_msrrecord):
    mod_list = Modify(example_classifyed_msrrecord, {"MN": "TEST"})
    assert mod_list.modify(modify_dict_value()) == {
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
    assert mod_list.modify(modify_dict_value())["MN"] == "TEST"