from collections import defaultdict

import pytest


@pytest.fixture
def example_empty_data():
    return {}


@pytest.fixture
def example_classifyed_msrrecord():
    return {
        'KW': '[MSR:RECORD]',
        'NA': '1',
        'MN': 'M1234',
        'LB': 'BST_LIB_MSR',
        'MT': 'M_BIN',
        'ST': 'kurztext',
        'LT': 'Langtext',
        '?0': '',
        'AD': '128',
        'SB': '1',
        '?1': '',
        '?2': '',
        '?3': '',
        '?4': '2'
        }


@pytest.fixture
def example_classifyed_paradata():
    return {
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


@pytest.fixture
def example_classifyed_uidacc():
    return {
        'KW': '[UID:ACCMSR]',
        'LEN': '5',
        'USER1': {
            'USER': 'USER1',
            'ACC': '3'
            },
        'USER2': {
            'USER': 'USER2',
            'ACC': '3'
            },
        'GUEST': {
            'USER': 'GUEST',
            'ACC': '1'
            },
        'USER3': {
            'USER': 'USER3',
            'ACC': '1'
            },
        'USER4': {
            'USER': 'USER4',
            'ACC': '1'
            }
        }


@pytest.fixture
def example_classifyed_eamrecord():
    return {
        'KW': '[EAM:RECORD]',
        'NA': '1',
        'VN': '54321_IN1',
        '?0': '0',
        'DT': 'INT',
        'VT': 'Variabel',
        'PI': '1',
        'EX': '0'
        }


@pytest.fixture
def example_classifyed_msrref():
    return {'KW': '[LAD:MSR_REF]', 'MN': 'M54321_AIW'}


@pytest.fixture
def example_classifyed_pararef():
    return {'KW': '[LAD:PARA_REF]', 'VN': '0.1', 'DT': 'REAL', '?0': '0', 'PI': '0', 'VC': '1'}


@pytest.fixture
def example_classifyed_pbvobjpath():
    return {'KW': '[PBV:OBJPATH]', 'NA': '1', 'LB': 'FBSLBLT', 'FN': 'Standart'}


@pytest.fixture
def example_classifyed_gwy():
    return {
        'KW': '[GWY:ACCEAM]',
        'MN': '54321_AUF',
        'LEN': '1',
        'T164': {
            'GN': 'T164',
            'G1': '1',
            'G2': '1'
            },
        'O168': {
            'GN': 'O168',
            'G1': '3',
            'G2': '0'
            },
        'END': '1'
        }


@pytest.fixture
def example_classifyed_hw2blob():
    return {
        'KW':
        '[HW2_BLOB]',
        'DTMN':
        '104',
        'QC':
        '776',
        'DTMC': (
            'Unit_Diag_Bit(0) = "CI840 B error"', 'Unit_Diag_Bit(1) = "CI840 A error"',
            'Unit_Diag_Bit(3) = "Redundant power A Failure"', 'Unit_Diag_Bit(4) = "Redundant power B failure"',
            'Unit_Diag_Bit(6) = "Redundancy warning"', 'Unit_Diag_Bit(7) = "Station warning"',
            'Unit_Diag_Bit(8) = "Station address warning"', 'Unit_Diag_Bit(14) = "Redundant cable A error"',
            'Unit_Diag_Bit(15) = "Redundant cable B error"'
            )
        }


@pytest.fixture
def example_classifyed_pbnode():
    return {'KW': '[PB:NODE]', 'NA': '1', 'MT': 'DIGBLT', 'FN': 'AM_KFO'}


@pytest.fixture
def example_classifyed_beginiodescritpion():
    return {
        'KW': '[BEGIN_IODESCRIPTION]',
        'CN': 'M1_IN_Kanal_01',
        'IO': '0',
        'DT': '0',
        'UB': '2',
        'B': '0',
        'BL': '1',
        'VN': 'X110001_IN',
        'C': '',
        '?1': '2',
        '?2': '2',
        '?3': '205',
        '?4': '1',
        '?5': '254',
        '?6': '68',
        '?7': '241181488',
        '?8': '1424956'
        }
