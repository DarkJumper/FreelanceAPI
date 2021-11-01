import pytest

from freelanceapi.msr.MsrRef import MsrRef
from .ExampleRows import exmaple_empty_row, example_msrref_row
from .ClassifyedExample import example_empty_data, example_classifyed_msrref
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_MsrRef(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = MsrRef()
        mod_list._first_execute(exmaple_empty_row)


def test_WrongKey_MsrRef(example_msrref_row):
    with pytest.raises(WrongeKey):
        mod_list = MsrRef()
        data = example_msrref_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list._first_execute(test)


def test_get_dict_MsrRef(example_msrref_row):
    mod_list = MsrRef()
    mod_list._first_execute(example_msrref_row)
    assert mod_list.get_dict == {'KW': '[LAD:MSR_REF]', 'MN': 'M54321_AIW'}


def test_get_string_MsrRef(example_msrref_row):
    mod_list = MsrRef()
    mod_list._first_execute(example_msrref_row)
    assert mod_list.get_string == example_msrref_row


def test_dict_to_string_MsrRef(example_classifyed_msrref, example_msrref_row):
    mod_list = MsrRef()
    mod_list.dict_to_string(example_classifyed_msrref)
    assert mod_list.get_string == example_msrref_row
    assert mod_list.get_dict == example_classifyed_msrref


def test_string_to_dict_MsrRef(example_classifyed_msrref, example_msrref_row):
    mod_list = MsrRef()
    mod_list.string_to_dict(example_msrref_row)
    assert mod_list.get_string == example_msrref_row
    assert mod_list.get_dict == example_classifyed_msrref


def test_string_to_dict_WrongeData_MsrRef(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = MsrRef()
        mod_list.string_to_dict(exmaple_empty_row)


def test_string_to_dict_WrongKey_MsrRef(example_msrref_row):
    with pytest.raises(WrongeKey):
        mod_list = MsrRef()
        data = example_msrref_row.split(";")
        data[0] = "TEST"
        test = ";".join(data)
        mod_list.string_to_dict(test)


def test_dict_to_string_WrongeData_MsrRef(example_empty_data):
    with pytest.raises(WrongeData):
        mod_list = MsrRef()
        mod_list.dict_to_string(example_empty_data)


def test_dict_to_string_WrongKey_MsrRef(example_classifyed_msrref):
    with pytest.raises(WrongeKey):
        mod_list = MsrRef()
        test = example_classifyed_msrref
        test['KW'] = "TEST"
        mod_list.dict_to_string(test)