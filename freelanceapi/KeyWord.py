from typing import Dict
from abc import ABC, abstractmethod, abstractproperty

from .utils.Classify import Classify, dict_zip_data
from .utils.Create import Create, create_string_from_dict_with_string
from .utils.Exceptions import WrongeKey, WrongeData


class KeyWord(ABC):

    @abstractmethod
    def _first_execute(self) -> None:
        pass

    @abstractmethod
    def string_to_dict(self) -> None:
        pass

    @abstractmethod
    def dict_to_string(self) -> None:
        pass

    @abstractproperty
    def get_dict(self) -> Dict:
        pass

    @abstractproperty
    def get_string(self) -> str:
        pass


class BaseClass(KeyWord):
    data_as_dict: Dict = dict()
    data_as_string: str = str()
    keys: list[str] = []
    expected_key: str = ""

    def _first_execute(self, new_data_string: str, sep: str = ";") -> None:
        self.string_to_dict(new_data_string, sep=sep)
        self.data_as_string = new_data_string

    def string_to_dict(self, new_data_string: str, sep: str = ";") -> None:
        self.data_as_dict = {}
        splitted_data = new_data_string.split(sep)
        if not new_data_string:
            raise WrongeData(" ".join(splitted_data), "Dataset is incorrect!")
        if splitted_data[0] != self.expected_key:
            raise WrongeKey(self.expected_key, splitted_data[0], "The key contained in the string does not match!")
        classify = Classify(splitted_data)
        self.data_as_dict.update(classify.execute(dict_zip_data(self.keys)))

    def dict_to_string(self, new_data_dict: Dict[str, Dict[str, str]], sep: str = ";") -> None:
        self.data_as_string = ""
        if not new_data_dict:
            raise WrongeData(" ".join(new_data_dict), "Dataset is incorrect!")
        if new_data_dict["KW"] != self.expected_key:
            raise WrongeKey(self.expected_key, new_data_dict["KW"], "The key contained in the string does not match!")
        created_string = Create(self.data_as_dict)
        self.data_as_string = created_string.string(create_string_from_dict_with_string())

    @property
    def get_dict(self) -> Dict[str, str]:
        return self.data_as_dict

    @property
    def get_string(self) -> str:
        return self.data_as_string
