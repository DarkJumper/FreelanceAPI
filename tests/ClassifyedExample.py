from collections import defaultdict

import pytest


@pytest.fixture
def example_empty_data():
    return {}


@pytest.fixture
def example_classifyed_msrrecord():
    return {
        'ID': '[MSR:RECORD]',
        'NA': '1',
        'MN': 'M1234',
        'LB': 'BST_LIB_MSR',
        'MT': 'M_BIN',
        'ST': 'kurztext',
        'LT': 'Langtext',
        'NI1': '',
        'AD': '128',
        'SB': '1',
        'NI2': '',
        'NI3': '',
        'NI4': '',
        'NI5': '2'
        }


@pytest.fixture
def example_classifyed_paradata():
    return {
        'ID':
        '[PARA:PARADATA]',
        'LEN':
        '28',
        'PARA': [
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
                                                                                                        },
            {
                'KN': 'ITt1',
                'L1': '7',
                'K1': 'DMSTIME',
                'L2': '0',
                'K2': ''
                }, {
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
        }


@pytest.fixture
def example_classifyed_uidacc():
    return {
        "ID":
        "[UID:ACCMSR]",
        "LEN":
        "5",
        "PARA": [
            {
                "USER": "USER1",
                "ACC": "3"
                }, {
                    "USER": "USER2",
                    "ACC": "3"
                    }, {
                        "USER": "GUEST",
                        "ACC": "1"
                        }, {
                            "USER": "USER3",
                            "ACC": "1"
                            }, {
                                "USER": "USER4",
                                "ACC": "1"
                                }
            ]
        }


@pytest.fixture
def example_classifyed_eamrecord():
    return {
        'ID': '[EAM:RECORD]',
        'NA': '1',
        'VN': '54321_IN1',
        'NI1': '0',
        'DT': 'INT',
        'VT': 'Variabel',
        'PI': '1',
        'EX': '0'
        }


@pytest.fixture
def example_classifyed_msrref():
    return {'ID': '[LAD:MSR_REF]', 'MN': 'M54321_AIW'}


@pytest.fixture
def example_classifyed_pararef():
    return {'ID': '[LAD:PARA_REF]', 'VN': '0.1', 'DT': 'REAL', 'NI1': '0', 'PI': '0', 'VC': '1'}


@pytest.fixture
def example_classifyed_pbvobjpath():
    return {'ID': '[PBV:OBJPATH]', 'NA': '1', 'LB': 'FBSLBLT', 'FN': 'Standart'}


@pytest.fixture
def example_classifyed_gwy():
    return {
        'ID': '[GWY:ACCEAM]',
        'MN': '54321_AUF',
        'LEN': '1',
        'PARA': [{
            'GN': 'T164',
            'G1': '1',
            'G2': '1'
            }, {
                'GN': 'O168',
                'G1': '3',
                'G2': '0'
                }],
        'END': '1'
        }


@pytest.fixture
def example_classifyed_hw2blob():
    return {
        'ID':
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
    return {'ID': '[PB:NODE]', 'NA': '1', 'MT': 'DIGBLT', 'FN': 'AM_KFO'}


@pytest.fixture
def example_classifyed_beginiodescritpion():
    return {
        'ID': '[BEGIN_IODESCRIPTION]',
        'CN': 'M1_IN_Kanal_01',
        'IO': '0',
        'DT': '0',
        'UB': '2',
        'B': '0',
        'BL': '1',
        'VN': 'X110001_IN',
        'C': '',
        'NI1': '2',
        'NI2': '2',
        'NI3': '205',
        'NI4': '1',
        'NI5': '254',
        'NI6': '68',
        'NI7': '241181488',
        'NI8': '1424956'
        }


@pytest.fixture
def example_classifyed_area():
    return {"ID": "[AREA]", "NA": "1", "AC": "!", "LA": "13", "AN": "Systembereich"}


@pytest.fixture
def example_classifyed_eamres():
    return {'ID': '[EAM:RESOURCEASSOCIATION]', 'NA': '1', 'VN': 'M1234', 'PS': 'PS19'}
