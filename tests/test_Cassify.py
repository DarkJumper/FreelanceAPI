import pytest
from freelanceapi.utils import (Classify, KeysDoNotMatchLength, dict_zip_data,
                                list_of_dict, tuple_of_decode_ascii_code)

from .ExampleRows import (example_msrrecord_row, example_paradata_row,
                          exmaple_hw2blob_row)


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
            'KN': 'OScan',
            'L1': '5',
            'K1': 'CHECK',
            'L2': '1',
            'K2': 'j'
            }, {
                'KN': 'Bt0',
                'L1': '5',
                'K1': 'MTEXT',
                'L2': '7',
                'K2': 'STÖRUNG'
                }, {
                    'KN': 'Bt1',
                    'L1': '5',
                    'K1': 'MTEXT',
                    'L2': '6',
                    'K2': 'BEREIT'
                    }, {
                        'KN': 'Mon',
                        'L1': '5',
                        'K1': 'CHECK',
                        'L2': '1',
                        'K2': 'j'
                        }, {
                            'KN': 'Mp',
                            'L1': '5',
                            'K1': 'MPRIO',
                            'L2': '1',
                            'K2': '2'
                            }, {
                                'KN': 'Mt',
                                'L1': '5',
                                'K1': 'MTEXT',
                                'L2': '6',
                                'K2': 'BEREIT'
                                }, {
                                    'KN': 'Wav1',
                                    'L1': '5',
                                    'K1': 'HTEXT',
                                    'L2': '0',
                                    'K2': ''
                                    }, {
                                        'KN': 'Gt',
                                        'L1': '13',
                                        'K1': 'CUSTSELLIST_2',
                                        'L2': '1',
                                        'K2': '0'
                                        }, {
                                            'KN': 'Ast',
                                            'L1': '5',
                                            'K1': 'ASTAT',
                                            'L2': '0',
                                            'K2': ''
                                            }, {
                                                'KN': 'Ht1',
                                                'L1': '5',
                                                'K1': 'HTEXT',
                                                'L2': '0',
                                                'K2': ''
                                                }, {
                                                    'KN': 'Bz',
                                                    'L1': '3',
                                                    'K1': 'BZO',
                                                    'L2': '0',
                                                    'K2': ''
                                                    }, {
                                                        'KN': 'BEDSEL',
                                                        'L1': '5',
                                                        'K1': 'CHECK',
                                                        'L2': '0',
                                                        'K2': ''
                                                        }, {
                                                            'KN': 'ChgShw',
                                                            'L1': '5',
                                                            'K1': 'CHECK',
                                                            'L2': '0',
                                                            'K2': ''
                                                            }, {
                                                                'KN': 'Alex0',
                                                                'L1': '5',
                                                                'K1': 'CHECK',
                                                                'L2': '0',
                                                                'K2': ''
                                                                }, {
                                                                    'KN': 'Alq0',
                                                                    'L1': '5',
                                                                    'K1': 'CHECK',
                                                                    'L2': '0',
                                                                    'K2': ''
                                                                    }, {
                                                                        'KN': 'Alex1',
                                                                        'L1': '5',
                                                                        'K1': 'CHECK',
                                                                        'L2': '0',
                                                                        'K2': ''
                                                                        }, {
                                                                            'KN': 'Alq1',
                                                                            'L1': '5',
                                                                            'K1': 'CHECK',
                                                                            'L2': '0',
                                                                            'K2': ''
                                                                            }, {
                                                                                'KN': 'Lmz',
                                                                                'L1': '5',
                                                                                'K1': 'CHECK',
                                                                                'L2': '0',
                                                                                'K2': ''
                                                                                }, {
                                                                                    'KN': 'Aval',
                                                                                    'L1': '5',
                                                                                    'K1': 'CHECK',
                                                                                    'L2': '0',
                                                                                    'K2': ''
                                                                                    }, {
                                                                                        'KN': 'Init',
                                                                                        'L1': '5',
                                                                                        'K1': 'CHECK',
                                                                                        'L2': '0',
                                                                                        'K2': ''
                                                                                        }, {
                                                                                            'KN': 'Acnt',
                                                                                            'L1': '4',
                                                                                            'K1': 'WORD',
                                                                                            'L2': '0',
                                                                                            'K2': ''
                                                                                            }, {
                                                                                                'KN': 'Align',
                                                                                                'L1': '4',
                                                                                                'K1': 'WORD',
                                                                                                'L2': '0',
                                                                                                'K2': ''
                                                                                                }, {
                                                                                                    'KN': 'ATt1',
                                                                                                    'L1': '7',
                                                                                                    'K1': 'DMSTIME',
                                                                                                    'L2': '0',
                                                                                                    'K2': ''
                                                                                                    }, {
                                                                                                        'KN': 'ITt1',
                                                                                                        'L1': '7',
                                                                                                        'K1': 'DMSTIME',
                                                                                                        'L2': '0',
                                                                                                        'K2': ''
                                                                                                        },
        {
            'KN': 'CAst1',
            'L1': '4',
            'K1': 'BYTE',
            'L2': '0',
            'K2': ''
            }, {
                'KN': 'OAst1',
                'L1': '4',
                'K1': 'BYTE',
                'L2': '0',
                'K2': ''
                }, {
                    'KN': 'Nlst1',
                    'L1': '4',
                    'K1': 'BYTE',
                    'L2': '0',
                    'K2': ''
                    }, {
                        'KN': 'Align1',
                        'L1': '4',
                        'K1': 'BYTE',
                        'L2': '0',
                        'K2': ''
                        }
        ]


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
