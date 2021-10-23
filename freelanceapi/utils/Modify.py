from typing import Callable, Dict

from .Exceptions import KeyNotFoundError

ModifyListStrategy = Callable[[Dict[str, str], list[str]], Dict]


def modify_dict_with_list() -> ModifyListStrategy:

    def modify_list_value(current_dict: Dict[str, list[str]], new_value: Dict[str, str]) -> Dict[str, list[str]]:
        """
        modify_list_value The values in the dict are changed. The last element are always changed. 

        Args:
            current_dict (Dict[str, list[str]]): dict to be modified. It has to pass a list of items. The list contains 2 items. It musst be a default dict!
            new_value (Dict[str, str]): dict with new data

        Raises:
            KeyNotFoundError: Key was not found in generated keys.

        Returns:
            Dict[str, list[str]]: Dict with changed values will be passed.
        """
        new_dict: Dict = current_dict
        for key in new_value:
            if current_dict[key] is None:
                raise KeyNotFoundError(key, "key is not included or incorrect!")
            new_list: list[str] = current_dict[key]
            # maybe exception  for to long lists
            new_list[-1] = new_value[key]
            new_dict[key] = new_list
        return new_dict

    return modify_list_value


def modify_dict_with_list_of_values() -> ModifyListStrategy:

    def modify_list_of_values(current_dict: Dict[str, list[str]], new_value: Dict[str, str]) -> Dict[str, list[str]]:
        """
        modify_list_of_values   The values in the dict are changed. The second last and the last element are always changed. 
                                                The second to last element is always the length of the last element, therefore only the last element must be passed.

        Args:
            current_dict (Dict[str, list[str]]): dict to be modified. It has to pass a list of items. The list contains 5 items. It musst be a default dict!
            new_value (Dict[str, str]): dict with new data

        Raises:
            KeyNotFoundError: Key was not found in generated keys.

        Returns:
            Dict[str, list[str]]: Dict with changed values will be passed.
        """
        new_dict: Dict = current_dict
        for key in new_value:
            if current_dict[key] is None:
                raise KeyNotFoundError(key, "key is not included or incorrect!")
            new_list: list[str] = current_dict[key]
            # maybe exception  for to long lists
            new_list[3:5] = [str(len(new_value[key])), new_value[key]]
            new_dict[key] = new_list
        return new_dict

    return modify_list_of_values


def modify_dict_value() -> ModifyListStrategy:

    def modify_item_value(current_dict: Dict[str, str], new_value: Dict[str, str]) -> Dict[str, str]:
        """
        modify_items_value values in dict are changed. According to the new_value dict.

        Args:
            current_dict (Dict[str, str]): dict to be modified.  It musst be a default dict!
            new_value (Dict[str, str]): dict with new data

        Raises:
            KeyNotFoundError: Key was not found in generated keys.

        Returns:
            Dict[str, str]: Dict with changed values will be passed.
        """
        new_dict: Dict = current_dict
        for key in new_value:
            if current_dict[key] is None:
                raise KeyNotFoundError(key, "key is not included or incorrect!")
            new_dict[key] = new_value[key]
        return new_dict

    return modify_item_value


class Modify:

    def __init__(self, current_dict: Dict[str, str], new_value: list[str]) -> None:
        self.new_value = new_value
        self.current_dict = current_dict

    def modify(self, used_strategy: ModifyListStrategy) -> ModifyListStrategy:
        return used_strategy(self.current_dict, self.new_value)
