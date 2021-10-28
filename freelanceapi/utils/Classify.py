from typing import Callable, Dict

from .Exceptions import KeysDoNotMatch

ClassifyerStrategy = Callable[[list[str]], Dict]


def dict_with_value_as_list(secondary_keys: list[str] = [], range_of_list: int = 5) -> ClassifyerStrategy:
    """
    Args:
        secondary_keys(list[str], optional): a list of keys for the inner dict. normaly the list is empty.
        range_of_list (int, optional): Lists size can be modified like this. Defaults to 5.
    """

    def splitted_value_as_list(dataset: list[str]) -> Dict[str, list[str]]:
        """
        splitted_value_as_list List is divided into the defined size!

        Args:
            dataset (list[str]): Data set contains all data key and associated data

        Returns:
            Dict[str, list[str]]:  Daten werden in einem dict mit einer liste als value 
        """
        print(len(dataset))
        print(range_of_list)
        if len(dataset) % range_of_list:
            raise KeysDoNotMatch(range_of_list, "The specified length of the list does not match the dataset!")
        result_dict: Dict = dict()
        for count, data in enumerate(dataset, start=0):
            if count % range_of_list == 0:
                result_dict[data] = dict(zip(secondary_keys, dataset[count:count + range_of_list]))
        return result_dict

    return splitted_value_as_list


def dict_zip_data(dict_keys: list[str] = []) -> ClassifyerStrategy:
    """
    Args:
        dict_keys (list[str]): List of key names!
    """

    def zip_data_with_keys(dataset: list[str]) -> Dict[str, str]:
        if len(dataset) != len(dict_keys):
            raise KeysDoNotMatch(
                ",".join(dict_keys), "The length of the keys does not match the length of the entered data"
                )
        return dict(zip(dict_keys, dataset))

    return zip_data_with_keys


class Classify:

    def __init__(self, data: list[str]) -> None:
        self.data = data

    def execute(self, used_strategy: ClassifyerStrategy) -> ClassifyerStrategy:
        return used_strategy(self.data)
