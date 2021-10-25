from typing import Dict
from collections import defaultdict
from abc import ABC, abstractmethod, abstractproperty

from .utils.Classify import Classify, dict_zip_data
from .utils.Modify import Modify, modify_dict_value
from .utils.Create import Create, create_string_from_dict_with_string
from .utils.Exceptions import WrongeKey, WrongeData


class KeyWord(ABC):

    @abstractmethod
    def evaluate_list(self) -> Dict:
        pass

    @abstractmethod
    def modify_parameter(self) -> str:
        pass

    @abstractproperty
    def get_dict(self) -> Dict:
        pass

    @abstractproperty
    def get_string(self) -> Dict:
        pass


class BaseClass(KeyWord):
    classifyed_data: Dict = defaultdict(lambda: None)
    keys: list[str] = []
    expected_key: str = ""

    def evaluate_list(self, list_of_data: list[str]) -> Dict:
        if not list_of_data:
            raise WrongeData(" ".join(list_of_data), "Dataset is incorrect!")
        if list_of_data[0] != self.expected_key:
            raise WrongeKey(self.expected_key, list_of_data[0], "The key contained in the string does not match!")
        classify = Classify(list_of_data)
        self.classifyed_data.update(classify.execute(dict_zip_data(self.keys)))

    def modify_parameter(self, new_value_of_key: Dict) -> str:
        mod_list = Modify(self.classifyed_data, new_value_of_key)
        self.classifyed_data.update(mod_list.modify(modify_dict_value()))

    @property
    def get_dict(self) -> Dict[str, list[str]]:
        return dict(self.classifyed_data)

    @property
    def get_string(self) -> str:
        created_string = Create(self.classifyed_data)
        return created_string.string(create_string_from_dict_with_string())