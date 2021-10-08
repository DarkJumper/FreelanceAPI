import pytest

from freelanceapi.utils.Classify import Classify, dict_with_value_as_list, dict_zip_data
from .ExampleList import exmaple_empty_list, example_paradata_list, example_msrrecord_list
from freelanceapi.utils.Exceptions import KeysDoNotMatch


def test_empty_dict_with_value_as_list(exmaple_empty_list):
    classify = Classify(exmaple_empty_list)
    assert classify.execute(dict_with_value_as_list(4)) == {}


def test_KeysDoNotMatch_dict_with_value_as_list(example_paradata_list):
    with pytest.raises(KeysDoNotMatch):
        classify = Classify(example_paradata_list)
        assert classify.execute(dict_with_value_as_list(6)) == {}
        classify = Classify(example_paradata_list.pop())
        assert classify.execute(dict_with_value_as_list(5)) == {}


def test_dict_with_value_as_list(example_paradata_list):
    classify = Classify(example_paradata_list)
    assert classify.execute(dict_with_value_as_list(5)) == {
        'OScan': ['OScan', '5', 'CHECK', '1', 'j'],
        'Bt0': ['Bt0', '5', 'MTEXT', '7', 'STÖRUNG'],
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
    assert classify.execute(dict_with_value_as_list(5))["Bt0"] == ['Bt0', '5', 'MTEXT', '7', 'STÖRUNG']


def test_empty_dict_zip_data(exmaple_empty_list):
    classify = Classify(exmaple_empty_list)
    assert classify.execute(dict_zip_data()) == {}


def test_KeysDoNotMatch_dict_zip_data(example_msrrecord_list):
    keys = ["MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    with pytest.raises(KeysDoNotMatch):
        classify = Classify(example_msrrecord_list)
        assert classify.execute(dict_zip_data(keys.pop())) == {}
        classify = Classify(example_msrrecord_list.pop())
        assert classify.execute(dict_zip_data(keys)) == {}


def test_dict_with_value_as_list(example_msrrecord_list):
    keys = ["MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    classify = Classify(example_msrrecord_list)
    assert classify.execute(dict_zip_data(keys)) == {
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
    assert classify.execute(dict_zip_data(keys))["MN"] == "M1234"