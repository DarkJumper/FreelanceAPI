from typing import Callable, Dict, Optional

CreateStringStrategy = Callable[[list[str]], Dict]


def create_string_from_dict_with_dict(sep: Optional[str] = ";") -> CreateStringStrategy:

    def create_from_dict(dataset: dict[str, list[str]]) -> str:
        """
        create_string_from_list Create a new string based on the passed data.

        Args:
            dataset (dict[str, list[str]]): a defultdict must be passed otherwise unforeseen errors will occur.

        Returns:
            str: newly created string. Each word is separated with semicolons (csv)
        """
        list_of_elements: list[str] = list()
        for key, data in dataset.items():
            if key in ["KW", "LEN", "MN", "END"]:
                list_of_elements += [dataset[key]]
                continue
            for element in data:
                list_of_elements += [data[element]]
        return f'{sep}'.join(list_of_elements)

    return create_from_dict


def create_string_from_dict_with_string(sep: Optional[str] = ";") -> CreateStringStrategy:

    def create_from_str(dataset: dict[str, str]) -> str:
        """
        create_from_str Create a new string based on the passed data.

        Args:
            dataset (dict[str, str]): a defultdict must be passed otherwise unforeseen errors will occur.

        Returns:
            str: newly created string. Each word is separated with semicolons (csv)
        """

        list_of_elements: list[str] = list()
        for key in dataset:
            list_of_elements += [dataset[key]]
        return f'{sep}'.join(list_of_elements)

    return create_from_str


class Create:

    def __init__(self, data: Dict[str, str]) -> None:
        self.data = data

    def string(self, used_strategy: CreateStringStrategy) -> CreateStringStrategy:
        return used_strategy(self.data)
