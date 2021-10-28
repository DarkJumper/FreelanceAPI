from freelanceapi.utils.Create import Create, create_string_from_dict_with_dict, create_string_from_dict_with_string
from .ClassifyedExample import example_classifyed_paradata, example_classifyed_msrrecord, example_empty_data


def test_create_string_from_dict_with_dict(example_classifyed_paradata, example_empty_data):
    created_string = Create(example_classifyed_paradata)
    created_sec_string = Create(example_empty_data)
    assert created_string.string(
        create_string_from_dict_with_dict()
        ) == "[PARA:PARADATA];28;OScan;5;CHECK;1;j;Bt0;5;MTEXT;7;STÖRUNG;Bt1;5;MTEXT;6;BEREIT;Mon;5;CHECK;1;j;Mp;5;MPRIO;1;2;Mt;5;MTEXT;6;BEREIT;Wav1;5;HTEXT;0;;Gt;13;CUSTSELLIST_2;1;0;Ast;5;ASTAT;0;;Ht1;5;HTEXT;0;;Bz;3;BZO;0;;BEDSEL;5;CHECK;0;;ChgShw;5;CHECK;0;;Alex0;5;CHECK;0;;Alq0;5;CHECK;0;;Alex1;5;CHECK;0;;Alq1;5;CHECK;0;;Lmz;5;CHECK;0;;Aval;5;CHECK;0;;Init;5;CHECK;0;;Acnt;4;WORD;0;;Align;4;WORD;0;;ATt1;7;DMSTIME;0;;ITt1;7;DMSTIME;0;;CAst1;4;BYTE;0;;OAst1;4;BYTE;0;;Nlst1;4;BYTE;0;;Align1;4;BYTE;0;"
    assert created_sec_string.string(create_string_from_dict_with_dict()) == ""


def test_create_string_from_dict_with_string(example_classifyed_msrrecord, example_empty_data):
    created_string = Create(example_classifyed_msrrecord)
    created_sec_string = Create(example_empty_data)
    assert created_string.string(
        create_string_from_dict_with_string()
        ) == "[MSR:RECORD];1;M1234;BST_LIB_MSR;M_BIN;kurztext;Langtext;;128;1;;;;2"
    assert created_sec_string.string(create_string_from_dict_with_string()) == ""