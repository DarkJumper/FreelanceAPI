import pytest

from freelanceapi.PbvObjpath import PbvObjpath
from .ExampleRows import exmaple_empty_row, example_pbvobjpath_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_PbvObjpath(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = PbvObjpath()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_PbvObjpath(example_pbvobjpath_row):
    with pytest.raises(WrongeKey):
        mod_list = PbvObjpath()
        data = example_pbvobjpath_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_PbvObjpath(example_pbvobjpath_row):
    mod_list = PbvObjpath()
    data = example_pbvobjpath_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {'LB': 'FBSLBLT', 'FN': 'Standart'}


def test_get_string_PbvObjpath(example_pbvobjpath_row):
    mod_list = PbvObjpath()
    data = example_pbvobjpath_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_pbvobjpath_row


def test_modify_PbvObjpath(example_pbvobjpath_row):
    mod_list = PbvObjpath()
    data = example_pbvobjpath_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"LB": "TEST"})
    assert mod_list.get_dict == {'LB': 'TEST', 'FN': 'Standart'}
    assert mod_list.get_string == "[PBV:OBJPATH];1;TEST;Standart"