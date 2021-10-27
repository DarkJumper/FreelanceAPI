import pytest

from freelanceapi.MsrRef import MsrRef
from .ExampleRows import exmaple_empty_row, example_msrref_row
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
