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


@pytest.fixture
def exmaple_hw2blob_row():
    return "[HW2_BLOB];104;776;55006E00690074005F0044006900610067005F0042006900740028003000290020003D0020002200430049003800340030002000420020006500720072006F00720022000D000A0055006E00690074005F0044006900610067005F0042006900740028003100290020003D0020002200430049003800340030002000410020006500720072006F00720022000D000A0055006E00690074005F0044006900610067005F0042006900740028003300290020003D002000220052006500640075006E00640061006E007400200070006F007700650072002000410020004600610069006C0075007200650022000D000A0055006E00690074005F0044006900610067005F0042006900740028003400290020003D002000220052006500640075006E00640061006E007400200070006F007700650072002000420020006600610069006C0075007200650022000D000A0055006E00690074005F0044006900610067005F0042006900740028003600290020003D002000220052006500640075006E00640061006E006300790020007700610072006E0069006E00670022000D000A0055006E00690074005F0044006900610067005F0042006900740028003700290020003D0020002200530074006100740069006F006E0020007700610072006E0069006E00670022000D000A0055006E00690074005F0044006900610067005F0042006900740028003800290020003D0020002200530074006100740069006F006E002000610064006400720065007300730020007700610072006E0069006E00670022000D000A0055006E00690074005F0044006900610067005F00420069007400280031003400290020003D002000220052006500640075006E00640061006E00740020006300610062006C0065002000410020006500720072006F00720022000D000A0055006E00690074005F0044006900610067005F00420069007400280031003500290020003D002000220052006500640075006E00640061006E00740020006300610062006C0065002000420020006500720072006F00720022000D000A000000"


@pytest.fixture
def exmaple_pbnode_row():
    return "[PB:NODE];1;DIGBLT;AM_KFO"


@pytest.fixture
def example_beginiodescription_row():
    return "[BEGIN_IODESCRIPTION];M1_IN_Kanal_01;0;0;2;0;1;X110001_IN;;2;2;205;1;254;68;241181488;1424956"


@pytest.fixture
def example_area_row():
    return "[AREA];1;!;13;Systembereich"


@pytest.fixture
def example_eamres_row():
    return "[EAM:RESOURCEASSOCIATION];1;M1234;PS19"
