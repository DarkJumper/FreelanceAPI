import pytest


@pytest.fixture
def exmaple_empty_row():
    return ""


@pytest.fixture
def example_msrrecord_row():
    return "[MSR:RECORD];1;M1234;BST_LIB_MSR;M_BIN;kurztext;Langtext;;128;1;;;;2"


@pytest.fixture
def example_paradata_row():
    return "[PARA:PARADATA];28;OScan;5;CHECK;1;j;Bt0;5;MTEXT;7;STÖRUNG;Bt1;5;MTEXT;6;BEREIT;Mon;5;CHECK;1;j;Mp;5;MPRIO;1;2;Mt;5;MTEXT;6;BEREIT;Wav1;5;HTEXT;0;;Gt;13;CUSTSELLIST_2;1;0;Ast;5;ASTAT;0;;Ht1;5;HTEXT;0;;Bz;3;BZO;0;;BEDSEL;5;CHECK;0;;ChgShw;5;CHECK;0;;Alex0;5;CHECK;0;;Alq0;5;CHECK;0;;Alex1;5;CHECK;0;;Alq1;5;CHECK;0;;Lmz;5;CHECK;0;;Aval;5;CHECK;0;;Init;5;CHECK;0;;Acnt;4;WORD;0;;Align;4;WORD;0;;ATt1;7;DMSTIME;0;;ITt1;7;DMSTIME;0;;CAst1;4;BYTE;0;;OAst1;4;BYTE;0;;Nlst1;4;BYTE;0;;Align1;4;BYTE;0;"


@pytest.fixture
def example_uidacc_row():
    return "[UID:ACCMSR];5;USER1;3;USER2;3;GUEST;1;USER3;1;USER4;1"


@pytest.fixture
def example_eamrecord_row():
    return "[EAM:RECORD];1;54321_IN1;0;INT;Variabel;1;0"


@pytest.fixture
def example_pbvobjpath_row():
    return "[PBV:OBJPATH];1;FBSLBLT;Standart"


@pytest.fixture
def example_msrref_row():
    return "[LAD:MSR_REF];M54321_AIW"


@pytest.fixture
def example_pararef_row():
    return "[LAD:PARA_REF];0.1;REAL;0;0;1"


@pytest.fixture
def example_gwy_row():
    return "[GWY:ACCEAM];54321_AUF;1;T164;1;1;O168;3;0;1"