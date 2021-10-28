import pytest

from freelanceapi.PbvObjpath import PbvObjpath
from .ExampleRows import exmaple_empty_row, example_pbvobjpath_row
from .ClassifyedExample import example_empty_data, example_classifyed_pbvobjpath
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_PbvObjpath(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = PbvObjpath()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_PbvObjpath(example_pbvobjpath_row):
    with pytest.raises(WrongeKey):
        mod_list = PbvObjpath()
        data = example_pbvobjpath_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_PbvObjpath(example_pbvobjpath_row):
    mod_list = PbvObjpath()
    mod_list._first_execute(example_pbvobjpath_row)
    assert mod_list.get_dict == {'KW': '[PBV:OBJPATH]', 'LEN': '1', 'LB': 'FBSLBLT', 'FN': 'Standart'}


def test_get_string_PbvObjpath(example_pbvobjpath_row):
    mod_list = PbvObjpath()
    mod_list._first_execute(example_pbvobjpath_row)
    assert mod_list.get_string == example_pbvobjpath_row


def test_dict_to_string_PbvObjpath(example_classifyed_pbvobjpath, example_pbvobjpath_row):
    mod_list = PbvObjpath()
    mod_list.dict_to_string(example_classifyed_pbvobjpath)
    assert mod_list.get_string == example_pbvobjpath_row
    assert mod_list.get_dict == example_classifyed_pbvobjpath


def test_string_to_dict_PbvObjpath(example_classifyed_pbvobjpath, example_pbvobjpath_row):
    mod_list = PbvObjpath()
    mod_list.string_to_dict(example_pbvobjpath_row)
    assert mod_list.get_string == example_pbvobjpath_row
    assert mod_list.get_dict == example_classifyed_pbvobjpath


def test_string_to_dict_WrongeData_PbvObjpath(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = PbvObjpath()
        mod_list.string_to_dict(exmaple_empty_row)


def test_string_to_dict_WrongKey_PbvObjpath(example_pbvobjpath_row):
    with pytest.raises(WrongeKey):
        mod_list = PbvObjpath()
        data = example_pbvobjpath_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.string_to_dict(test)


def test_dict_to_string_WrongeData_PbvObjpath(example_empty_data):
    with pytest.raises(WrongeData):
        mod_list = PbvObjpath()
        mod_list.dict_to_string(example_empty_data)


def test_dict_to_string_WrongKey_PbvObjpath(example_classifyed_pbvobjpath):
    with pytest.raises(WrongeKey):
        mod_list = PbvObjpath()
        test = example_classifyed_pbvobjpath
        test['KW'] = "TEST"
        mod_list.dict_to_string(test)