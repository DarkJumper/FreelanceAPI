class KeyNotFoundError(Exception):
    """
    KeyNotFoundError Key in dict didn't exists or is incorect

    Args:
        Exception ([type]): Main Class for exceptions
    """

    def __init__(self, value, message: str = ""):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'


class KeysDoNotMatch(Exception):
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
