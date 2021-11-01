from typing import Dict

from .KeyWord import KeyWord
from ..utils.Classify import Classify, dict_with_value_as_list
from ..utils.Create import Create, create_string_from_dict_with_dict
from ..utils.Exceptions import WrongeKey, WrongeData


class UidAcc(KeyWord):
    data_as_dict: Dict = dict()
    data_as_string: str = str()
    expected_key = "[UID:ACCMSR]"
    keys: list[str] = ["USER", "ACC"]

    def _first_execute(self, new_data_string: str, sep: str = ";") -> None:
        self.string_to_dict(new_data_string, sep=sep)
        self.data_as_string = new_data_string

    def string_to_dict(self, new_data_string: str, sep: str = ";") -> Dict:
        self.data_as_dict = {}
        splitted_data = new_data_string.split(sep)
        if not new_data_string:
            raise WrongeData(",".join(splitted_data), "Dataset is incorrect!")
        self.data_as_dict["KW"], self.data_as_dict["LEN"], *parameter = splitted_data
        if splitted_data[0] != self.expected_key:
            raise WrongeKey(self.expected_key, splitted_data[0], "The key contained in the string does not match!")
        classify = Classify(parameter)
        self.data_as_dict.update(classify.execute(dict_with_value_as_list(self.keys, 2)))
        self.data_as_string = new_data_string

    def dict_to_string(self, new_data_dict: Dict[str, Dict[str, str]], sep: str = ";") -> None:
        self.data_as_string = ""
        if not new_data_dict:
            raise WrongeData(",".join(new_data_dict), "Dataset is incorrect!")
        if new_data_dict["KW"] != self.expected_key:
            raise WrongeKey(self.expected_key, new_data_dict["KW"], "The key contained in the string does not match!")
        created_string = Create(new_data_dict)
        self.data_as_string = created_string.string(create_string_from_dict_with_dict(sep=sep))
        self.data_as_dict = new_data_dict

    @property
    def get_dict(self) -> Dict[str, list[str]]:
        return self.data_as_dict

    @property
    def get_string(self) -> str:
        return self.data_as_string
