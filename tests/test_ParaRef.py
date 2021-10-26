import pytest

from freelanceapi.ParaRef import ParaRef
from .ExampleRows import exmaple_empty_row, example_pararef_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_ParaRef(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = ParaRef()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_ParaRef(example_pararef_row):
    with pytest.raises(WrongeKey):
        mod_list = ParaRef()
        data = example_pararef_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_ParaRef(example_pararef_row):
    mod_list = ParaRef()
    data = example_pararef_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {'KW': '[LAD:PARA_REF]', 'VN': '0.1', 'DT': 'REAL', '?0': '0', 'PI': '0', 'END': '1'}


def test_get_string_ParaRef(example_pararef_row):
    mod_list = ParaRef()
    data = example_pararef_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_pararef_row


def test_modify_ParaRef(example_pararef_row):
    mod_list = ParaRef()
    data = example_pararef_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"VN": "0.3"})
    assert mod_list.get_dict == {'KW': '[LAD:PARA_REF]', 'VN': '0.3', 'DT': 'REAL', '?0': '0', 'PI': '0', 'END': '1'}
    assert mod_list.get_string == "[LAD:PARA_REF];0.3;REAL;0;0;1"