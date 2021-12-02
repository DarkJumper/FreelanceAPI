import pytest
from freelanceapi.utils.Classify import (Classify, dict_with_value_as_list, dict_zip_data, tuple_of_decode_ascii_code)
from freelanceapi.utils.Exceptions import KeysDoNotMatchLength

from .ExampleRows import (example_msrrecord_row, example_paradata_row, exmaple_hw2blob_row)


def test_empty_dict_with_value_as_list():
    classify = Classify([])
    assert classify.execute(dict_with_value_as_list(4)) == {}


def test_KeysDoNotMatchLength_dict_with_value_as_list(example_paradata_row):
    splitted_data = example_paradata_row.split(";")
    with pytest.raises(KeysDoNotMatchLength):
        classify = Classify(splitted_data)
        assert classify.execute(dict_with_value_as_list(6)) == {}
        classify = Classify(splitted_data.pop())
        assert classify.execute(dict_with_value_as_list(5)) == {}


def test_dict_with_value_as_list(example_paradata_row):
    classify = Classify(example_paradata_row.split(";"))
    assert classify.execute(dict_with_value_as_list(["KN", "L1", "K1", "L2", "K2"], 5)) == {
        {
            'OScan': {
                'KN': 'OScan',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '1',
                'K2': 'j'
                },
            'Bt0': {
                'KN': 'Bt0',
                'L1': '5',
                'K1': 'MTEXT',
                'L2': '7',
                'K2': 'STÖRUNG'
                },
            'Bt1': {
                'KN': 'Bt1',
                'L1': '5',
                'K1': 'MTEXT',
                'L2': '6',
                'K2': 'BEREIT'
                },
            'Mon': {
                'KN': 'Mon',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '1',
                'K2': 'j'
                },
            'Mp': {
                'KN': 'Mp',
                'L1': '5',
                'K1': 'MPRIO',
                'L2': '1',
                'K2': '2'
                },
            'Mt': {
                'KN': 'Mt',
                'L1': '5',
                'K1': 'MTEXT',
                'L2': '6',
                'K2': 'BEREIT'
                },
            'Wav1': {
                'KN': 'Wav1',
                'L1': '5',
                'K1': 'HTEXT',
                'L2': '0',
                'K2': ''
                },
            'Gt': {
                'KN': 'Gt',
                'L1': '13',
                'K1': 'CUSTSELLIST_2',
                'L2': '1',
                'K2': '0'
                },
            'Ast': {
                'KN': 'Ast',
                'L1': '5',
                'K1': 'ASTAT',
                'L2': '0',
                'K2': ''
                },
            'Ht1': {
                'KN': 'Ht1',
                'L1': '5',
                'K1': 'HTEXT',
                'L2': '0',
                'K2': ''
                },
            'Bz': {
                'KN': 'Bz',
                'L1': '3',
                'K1': 'BZO',
                'L2': '0',
                'K2': ''
                },
            'BEDSEL': {
                'KN': 'BEDSEL',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'ChgShw': {
                'KN': 'ChgShw',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Alex0': {
                'KN': 'Alex0',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Alq0': {
                'KN': 'Alq0',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Alex1': {
                'KN': 'Alex1',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Alq1': {
                'KN': 'Alq1',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Lmz': {
                'KN': 'Lmz',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Aval': {
                'KN': 'Aval',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Init': {
                'KN': 'Init',
                'L1': '5',
                'K1': 'CHECK',
                'L2': '0',
                'K2': ''
                },
            'Acnt': {
                'KN': 'Acnt',
                'L1': '4',
                'K1': 'WORD',
                'L2': '0',
                'K2': ''
                },
            'Align': {
                'KN': 'Align',
                'L1': '4',
                'K1': 'WORD',
                'L2': '0',
                'K2': ''
                },
            'ATt1': {
                'KN': 'ATt1',
                'L1': '7',
                'K1': 'DMSTIME',
                'L2': '0',
                'K2': ''
                },
            'ITt1': {
                'KN': 'ITt1',
                'L1': '7',
                'K1': 'DMSTIME',
                'L2': '0',
                'K2': ''
                },
            'CAst1': {
                'KN': 'CAst1',
                'L1': '4',
                'K1': 'BYTE',
                'L2': '0',
                'K2': ''
                },
            'OAst1': {
                'KN': 'OAst1',
                'L1': '4',
                'K1': 'BYTE',
                'L2': '0',
                'K2': ''
                },
            'Nlst1': {
                'KN': 'Nlst1',
                'L1': '4',
                'K1': 'BYTE',
                'L2': '0',
                'K2': ''
                },
            'Align1': {
                'KN': 'Align1',
                'L1': '4',
                'K1': 'BYTE',
                'L2': '0',
                'K2': ''
                }
            }
        }


def test_empty_dict_zip_data():
    classify = Classify([])
    assert classify.execute(dict_zip_data()) == {}


def test_KeysDoNotMatchLength_dict_zip_data(example_msrrecord_row):
    keys = ["MN", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    splitted_data = example_msrrecord_row.split(";")
    with pytest.raises(KeysDoNotMatchLength):
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


def test_empty_tuple_of_decode_ascii_code():
    classify = Classify([])
    assert classify.execute(tuple_of_decode_ascii_code("")) == {"": ()}


def test_KeysDoNotMatchLength_tuple_of_decode_ascii_code(exmaple_hw2blob_row):
    splitted_data = exmaple_hw2blob_row.split(";")
    with pytest.raises(KeysDoNotMatchLength):
        classify = Classify(splitted_data.pop())
        assert classify.execute(tuple_of_decode_ascii_code("DTMC", 2)) == {}


def test_tuple_of_decode_ascii_code(exmaple_hw2blob_row):
    splitted_row = exmaple_hw2blob_row.split(";")
    classify = Classify(splitted_row.pop())
    assert classify.execute(tuple_of_decode_ascii_code("DTMC", splitted_row.pop())) == {
        'DTMC': (
            'Unit_Diag_Bit(0) = "CI840 B error"', 'Unit_Diag_Bit(1) = "CI840 A error"',
            'Unit_Diag_Bit(3) = "Redundant power A Failure"', 'Unit_Diag_Bit(4) = "Redundant power B failure"',
            'Unit_Diag_Bit(6) = "Redundancy warning"', 'Unit_Diag_Bit(7) = "Station warning"',
            'Unit_Diag_Bit(8) = "Station address warning"', 'Unit_Diag_Bit(14) = "Redundant cable A error"',
            'Unit_Diag_Bit(15) = "Redundant cable B error"'
            )
        }
