from typing import Dict
from abc import ABC, abstractmethod, abstractproperty


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