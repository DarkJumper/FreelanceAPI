import pytest

from freelanceapi.ParaData import ParaData
from .ExampleRows import exmaple_empty_row, example_paradata_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_ParaData(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = ParaData()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_ParaData(example_paradata_row):
    with pytest.raises(WrongeKey):
        mod_list = ParaData()
        data = example_paradata_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_ParaData(example_paradata_row):
    mod_list = ParaData()
    data = example_paradata_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {
        'KW': '[PARA:PARADATA]',
        'LEN': '28',
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


def test_get_string_ParaData(example_paradata_row):
    mod_list = ParaData()
    data = example_paradata_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_paradata_row


def test_modify_ParaData(example_paradata_row):
    mod_list = ParaData()
    data = example_paradata_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"Bt0": "TEST"})
    assert mod_list.get_dict == {
        'KW': '[PARA:PARADATA]',
        'LEN': '28',
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
    assert mod_list.get_string == "[PARA:PARADATA];28;OScan;5;CHECK;1;j;Bt0;5;MTEXT;4;TEST;Bt1;5;MTEXT;6;BEREIT;Mon;5;CHECK;1;j;Mp;5;MPRIO;1;2;Mt;5;MTEXT;6;BEREIT;Wav1;5;HTEXT;0;;Gt;13;CUSTSELLIST_2;1;0;Ast;5;ASTAT;0;;Ht1;5;HTEXT;0;;Bz;3;BZO;0;;BEDSEL;5;CHECK;0;;ChgShw;5;CHECK;0;;Alex0;5;CHECK;0;;Alq0;5;CHECK;0;;Alex1;5;CHECK;0;;Alq1;5;CHECK;0;;Lmz;5;CHECK;0;;Aval;5;CHECK;0;;Init;5;CHECK;0;;Acnt;4;WORD;0;;Align;4;WORD;0;;ATt1;7;DMSTIME;0;;ITt1;7;DMSTIME;0;;CAst1;4;BYTE;0;;OAst1;4;BYTE;0;;Nlst1;4;BYTE;0;;Align1;4;BYTE;0;"