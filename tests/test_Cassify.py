import pytest
from freelanceapi.utils import (Classify, KeysDoNotMatchLength, dict_zip_data, list_of_dict, tuple_of_decode_ascii_code)

from .ClassifyedExample import example_classifyed_paradata
from .ExampleRows import (example_msrrecord_row, example_paradata_row, exmaple_hw2blob_row)


def test_empty_list_of_dict():
    classify = Classify([])
    assert classify.execute(list_of_dict(4)) == []


def test_KeysDoNotMatchLength_dict_with_value_as_list(example_paradata_row):
    splitted_data = example_paradata_row.split(";")
    with pytest.raises(KeysDoNotMatchLength):
        classify = Classify(splitted_data)
        assert classify.execute(list_of_dict(6)) == {}
        classify = Classify(splitted_data.pop())
        assert classify.execute(list_of_dict(5)) == {}


def test_list_of_dict(example_paradata_row):
    _, _, *parameter = example_paradata_row.split(";")
    classify = Classify(parameter)
    assert classify.execute(list_of_dict(["KN", "L1", "K1", "L2", "K2"], 5)) == [
        {
            'KN': 'QUIT1',
            'L1': '11',
            'K1': 'CONFIRMFORM',
            'L2': '1',
            'K2': '1'
            }, {
                'KN': 'QUIT2',
                'L1': '11',
                'K1': 'CONFIRMFORM',
                'L2': '1',
                'K2': '1'
                }, {
                    'KN': 'QUIT3',
                    'L1': '11',
                    'K1': 'CONFIRMFORM',
                    'L2': '1',
                    'K2': '2'
                    }, {
                        'KN': 'QUIT4',
                        'L1': '11',
                        'K1': 'CONFIRMFORM',
                        'L2': '1',
                        'K2': '2'
                        }
        ]


def test_empty_dict_zip_data():
    classify = Classify([])
    assert classify.execute(dict_zip_data()) == {}


def test_KeysDoNotMatchLength_dict_zip_data(example_msrrecord_row):
    keys = ["MP", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    splitted_data = example_msrrecord_row.split(";")
    with pytest.raises(KeysDoNotMatchLength):
        classify = Classify(splitted_data)
        assert classify.execute(dict_zip_data(keys.pop())) == {}
        classify = Classify(splitted_data.pop())
        assert classify.execute(dict_zip_data(keys)) == {}


def test_dict_with_value_as_list(example_msrrecord_row):
    keys = ["KW", "LEN", "MP", "LIB", "BT", "KT", "LT", "?0", "PA", "ST", "?1", "?2", "?3", 'END']
    splitted_data = example_msrrecord_row.split(";")
    classify = Classify(splitted_data)
    assert classify.execute(dict_zip_data(keys)) == {
        'KW': '[MSR:RECORD]',
        'LEN': '1',
        'MP': 'M1234',
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
    assert classify.execute(dict_zip_data(keys))["MP"] == "M1234"


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
