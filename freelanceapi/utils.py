from typing import Callable, Dict, Tuple, Union


## Exceptions
class KeysDoNotMatchLength(Exception):
    """
    KeysDoNotMatch Length of Keys do not match with the dataset

    Args:
        Exception ([type]): Main Class for exceptions
    """

    def __init__(self, values: str, message: str = ""):
        self.values = values
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Value:{self.values}  -> Msg:{self.message}'


## Classifyer
ClassifyerStrategy = Callable[[Union[list[str], str]], Dict | list]


def list_of_dict(secondary_keys: list[str] = [], range_of_list: int = 5) -> ClassifyerStrategy:
    """
    Args:
        secondary_keys(list[str], optional): a list of keys for the inner dict. normaly the list is empty.
        range_of_list (int, optional): Lists size can be modified like this. Defaults to 5.
    """

    def splitted_value_as_list(dataset: list[str]) -> list[Dict[str, list]]:
        """
        splitted_value_as_list List is divided into the defined size!

        Args:
            dataset (list[str]): Data set contains all data key and associated data

        Returns:
            Dict[str, list[str]]:  Daten werden in einem dict mit einer liste als value 
        """
        if len(dataset) % int(range_of_list):
            raise KeysDoNotMatchLength(range_of_list, "The specified length of the list does not match the dataset!")
        return [
            dict(zip(secondary_keys, dataset[count:count + range_of_list]))
            for count, data in enumerate(dataset, start=0) if count % range_of_list == 0
            ]

    return splitted_value_as_list


def dict_zip_data(dict_keys: list[str] = []) -> ClassifyerStrategy:
    """
    Args:
        dict_keys (list[str]): List of key names!
    """

    def zip_data_with_keys(dataset: list[str]) -> Dict[str, str]:
        if len(dataset) != len(dict_keys):
            raise KeysDoNotMatchLength(
                ",".join(dict_keys), "The length of the keys does not match the length of the entered data"
                )
        return dict(zip(dict_keys, dataset))

    return zip_data_with_keys


def tuple_of_decode_ascii_code(dict_key: str = "", range_of_data: int = 0) -> ClassifyerStrategy:

    def decode_asccii(dataset: str) -> Dict[str, Tuple[str]]:
        """
        decode_asccii The ascii string is converted to a tuple and returned as a dict. All not needed information will be filtered out. After each Carriage Return (0D) the tuple is terminated.

        Args:
            dataset (str): A pure ascii string should be passed.

        Raises:
            KeysDoNotMatchLength: If the length specified does not match the length of the ascii data.

        Returns:
            Dict[str, Tuple[str]]: A dict with a given key and one or more tuples as value.
        """
        ascii_sentence: Tuple[str] = tuple()
        current_ascii_string = ""
        if len(dataset[::2]) != int(range_of_data):
            raise KeysDoNotMatchLength(
                range_of_data, "The length of the keys does not match the length of the entered data"
                )
        for char_count in range(0, int(range_of_data), 2):
            hex_ascii = dataset[char_count * 2:char_count*2 + 2]
            if hex_ascii == '0D':
                ## 0x0D 	CR:	Carriage Return
                ascii_sentence += (current_ascii_string.strip(), )
                current_ascii_string = ""
                continue
            bytes_object = bytes.fromhex(hex_ascii)
            current_ascii_string += bytes_object.decode("ASCII")
        return {dict_key: ascii_sentence}

    return decode_asccii


class Classify:

    def __init__(self, data: Union[list[str], str]) -> None:
        self.data = data

    def execute(self, used_strategy: ClassifyerStrategy) -> ClassifyerStrategy:
        return used_strategy(self.data)
