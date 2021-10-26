import pytest

from freelanceapi.MsrRef import MsrRef
from .ExampleRows import exmaple_empty_row, example_msrref_row
from freelanceapi.utils.Exceptions import WrongeData, WrongeKey


def test_WrongeData_MsrRef(exmaple_empty_row):
    with pytest.raises(WrongeData):
        mod_list = MsrRef()
        mod_list.evaluate_list(exmaple_empty_row)


def test_WrongKey_MsrRef(example_msrref_row):
    with pytest.raises(WrongeKey):
        mod_list = MsrRef()
        data = example_msrref_row.split(";")
        data[0] = "TEST"
        mod_list.evaluate_list(data)


def test_get_dict_MsrRef(example_msrref_row):
    mod_list = MsrRef()
    data = example_msrref_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_dict == {'KW': '[LAD:MSR_REF]', 'MN': 'M54321_AIW'}


def test_get_string_MsrRef(example_msrref_row):
    mod_list = MsrRef()
    data = example_msrref_row.split(";")
    mod_list.evaluate_list(data)
    assert mod_list.get_string == example_msrref_row


def test_modify_MsrRef(example_msrref_row):
    mod_list = MsrRef()
    data = example_msrref_row.split(";")
    mod_list.evaluate_list(data)
    mod_list.modify_parameter({"MN": "TEST"})
    assert mod_list.get_dict == {'KW': '[LAD:MSR_REF]', 'MN': 'TEST'}
    assert mod_list.get_string == "[LAD:MSR_REF];TEST"