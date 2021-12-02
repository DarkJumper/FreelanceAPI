from freelanceapi.utils.Create import (
    Create, create_ascii_hex, create_string_from_dict_with_dict, create_string_from_dict_with_string
    )

from .ClassifyedExample import (
    example_classifyed_hw2blob, example_classifyed_msrrecord, example_classifyed_paradata, example_empty_data
    )


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


def test_create_ascii_hex(example_classifyed_hw2blob):
    created_string = Create(example_classifyed_hw2blob.pop("DTMC"))
    created_sec_string = Create([])
    assert created_string.string(
        create_ascii_hex()
        ) == "55006E00690074005F0044006900610067005F0042006900740028003000290020003D0020002200430049003800340030002000420020006500720072006F00720022000D000A0055006E00690074005F0044006900610067005F0042006900740028003100290020003D0020002200430049003800340030002000410020006500720072006F00720022000D000A0055006E00690074005F0044006900610067005F0042006900740028003300290020003D002000220052006500640075006E00640061006E007400200070006F007700650072002000410020004600610069006C0075007200650022000D000A0055006E00690074005F0044006900610067005F0042006900740028003400290020003D002000220052006500640075006E00640061006E007400200070006F007700650072002000420020006600610069006C0075007200650022000D000A0055006E00690074005F0044006900610067005F0042006900740028003600290020003D002000220052006500640075006E00640061006E006300790020007700610072006E0069006E00670022000D000A0055006E00690074005F0044006900610067005F0042006900740028003700290020003D0020002200530074006100740069006F006E0020007700610072006E0069006E00670022000D000A0055006E00690074005F0044006900610067005F0042006900740028003800290020003D0020002200530074006100740069006F006E002000610064006400720065007300730020007700610072006E0069006E00670022000D000A0055006E00690074005F0044006900610067005F00420069007400280031003400290020003D002000220052006500640075006E00640061006E00740020006300610062006C0065002000410020006500720072006F00720022000D000A0055006E00690074005F0044006900610067005F00420069007400280031003500290020003D002000220052006500640075006E00640061006E00740020006300610062006C0065002000420020006500720072006F00720022000D000A000000"
    assert created_sec_string.string(create_ascii_hex()) == ""
