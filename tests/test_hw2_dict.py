import pytest
from freelanceapi.sections.hw2_dict import BeginIODescriptionDict, Hw2BlobDict

from .ClassifyedExample import (example_classifyed_beginiodescritpion, example_classifyed_hw2blob, example_empty_data)
from .ExampleRows import (example_beginiodescription_row, exmaple_empty_row, exmaple_hw2blob_row)


def test_Hw2BlobDict_prepare_merge(exmaple_hw2blob_row, example_classifyed_hw2blob):
    mod_list = Hw2BlobDict()
    assert mod_list.merge_dict(exmaple_hw2blob_row.split(";")) == example_classifyed_hw2blob


def test_BeginIODescriptionDict_prepare_merge(example_beginiodescription_row, example_classifyed_beginiodescritpion):
    mod_list = BeginIODescriptionDict()
    assert mod_list.merge_dict(example_beginiodescription_row.split(";")) == example_classifyed_beginiodescritpion
