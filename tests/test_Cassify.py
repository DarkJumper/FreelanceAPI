import pytest

from freelanceapi.utils.Classify import Classify, dict_with_value_as_list, dict_zip_data
from .ExampleRows import example_paradata_row, example_msrrecord_row
from freelanceapi.utils.Exceptions import KeysDoNotMatch


def test_empty_dict_with_value_as_list():
    classify = Classify([])
    assert classify.execute(dict_with_value_as_list(4)) == {}


def test_KeysDoNotMatch_dict_with_value_as_list(example_paradata_row):
    splitted_data = example_paradata_row.split(";")
    with pytest.raises(KeysDoNotMatch):
        classify = Classify(splitted_data)
        assert classify.execute(dict_with_value_as_list(6)) == {}
        classify = Classify(splitted_data.pop())
        assert classify.execute(dict_with_value_as_list(5)) == {}


def test_dict_with_value_as_list(example_paradata_row):
    classify = Classify(example_paradata_row.split(";"))
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


def test_empty_dict_zip_data():
    classify = Classify([])
    assert classify.execute(dict_zip_data()) == {}


def test_KeysDoNotMatch_dict_zip_data(example_msrrecord_row):
    keys = ["MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    splitted_data = example_msrrecord_row.split(";")
    with pytest.raises(KeysDoNotMatch):
        classify = Classify(splitted_data)
        assert classify.execute(dict_zip_data(keys.pop())) == {}
        classify = Classify(splitted_data.pop())
        assert classify.execute(dict_zip_data(keys)) == {}


def test_dict_with_value_as_list(example_msrrecord_row):
    keys = ["KW", "LEN", "MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    splitted_data = example_msrrecord_row.split(";")
    classify = Classify(splitted_data)
    assert classify.execute(dict_zip_data(keys)) == {
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
    assert classify.execute(dict_zip_data(keys))["MN"] == "M1234"