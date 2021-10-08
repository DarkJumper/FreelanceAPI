from typing import Callable, Dict

ClassifyerStrategy = Callable[[list[str]], Dict]


def value_as_list_strategy(range_of_list: int = 5) -> ClassifyerStrategy:

    def splitted_value_as_list(dataset: list[str]) -> Dict[str, list[str]]:
        result_dict: Dict = dict()
        for count, data in enumerate(dataset, start=0):
            if count % range_of_list == 0:
                result_dict[data] = dataset[count:count + range_of_list]
        return result_dict

    return splitted_value_as_list


def zip_data_strategy(dict_keys: list[str]) -> ClassifyerStrategy:

    def zip_data_with_keys(dataset: list[str]) -> Dict[str, str]:
        return dict(zip(dict_keys, dataset))

    return zip_data_with_keys


class Classify:

    def __init__(self, data: list[str]) -> None:
        self.data = data

    def execute(self, used_strategy: ClassifyerStrategy) -> ClassifyerStrategy:
        return used_strategy(self.data)
