from typing import Dict
from collections import defaultdict

from KeyWord import KeyWord
from utils.Classify import Classify, dict_with_value_as_list
from utils.Modify import Modify, modify_dict_with_list_of_values
from utils.Create import Create, create_string_from_dict_with_list
from utils.Exceptions import WrongeKey


class ParaData(KeyWord):
    classifyed_data: Dict = defaultdict(lambda: None)
    _key_word: str = ""
    _length: str = ""
    __expected_key = "[PARA:PARADATA]"

    def evaluate_list(self, row_of_data: str) -> Dict:
        self._key_word, self._length, *parameter = row_of_data.split(";")
        if self._key_word != self.__expected_key:
            raise WrongeKey(self.__expected_key, self._key_word, "The key contained in the string does not match!")
        classify = Classify(parameter)
        self.classifyed_data.update(classify.execute(dict_with_value_as_list(5)))

    def modify_parameter(self, new_value_of_key: Dict) -> str:
        mod_list = Modify(self.classifyed_data, new_value_of_key)
        self.classifyed_data.update(mod_list.modify(modify_dict_with_list_of_values()))

    @property
    def get_dict(self) -> Dict[str, list[str]]:
        return self.classifyed_data

    @property
    def get_string(self) -> str:
        created_string = Create(self.classifyed_data)
        new_string = created_string.string(create_string_from_dict_with_list())
        return f'{self._key_word};{self._length};{new_string}'