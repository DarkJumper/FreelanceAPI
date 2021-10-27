import pytest

from freelanceapi.ParaData import ParaData
from .ExampleRows import exmaple_empty_row, example_paradata_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_ParaData(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = ParaData()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_ParaData(example_paradata_row):
    with pytest.raises(WrongeKey):
        mod_list = ParaData()
        data = example_paradata_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_ParaData(example_paradata_row):
    mod_list = ParaData()
    mod_list._first_execute(example_paradata_row)
    assert mod_list.get_dict == {
        'KW': '[PARA:PARADATA]',
        'LEN': '28',
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


def test_get_string_ParaData(example_paradata_row):
    mod_list = ParaData()
    mod_list._first_execute(example_paradata_row)
    assert mod_list.get_string == example_paradata_row
