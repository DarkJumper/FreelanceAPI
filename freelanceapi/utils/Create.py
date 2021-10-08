from typing import Callable, Dict

CreateStringStrategy = Callable[[list[str]], Dict]


def create_string_from_dict_with_list() -> CreateStringStrategy:

    def create_from_list(dataset: dict[str, list[str]]) -> str:
        """
        create_string_from_list Create a new string based on the passed data.

        Args:
            dataset (dict[str, list[str]]): The length of the list is irrelevant.

        Returns:
            str: newly created string. Each word is separated with semicolons (csv)
        """
        list_of_elements: list[str] = list()
        for key in dataset:
            list_of_elements += dataset[key]
        return ";".join(list_of_elements)

    return create_from_list


def create_string_from_dict_with_string() -> CreateStringStrategy:

    def create_from_str(dataset: dict[str, str]) -> str:
        """
        create_from_str Create a new string based on the passed data.

        Args:
            dataset (dict[str, str])

        Returns:
            str: newly created string. Each word is separated with semicolons (csv)
        """
        list_of_elements: list[str] = list()
        for key in dataset:
            list_of_elements += [dataset[key]]
        return ";".join(list_of_elements)

    return create_from_str


class Create:

    def __init__(self, data: Dict[str, str]) -> None:
        self.data = data

    def string(self, used_strategy: CreateStringStrategy) -> CreateStringStrategy:
        return used_strategy(self.data)
