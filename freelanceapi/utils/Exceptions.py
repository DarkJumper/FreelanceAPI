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


class WrongeKey(Exception):
    """
    WrongeKey Key Word of the String ist Wronge

    Args:
        Exception ([type]): Main Class for exceptions
    """

    def __init__(self, key_word: str, current_keyword: str, message: str = ""):
        self.key_word = key_word
        self.current_keyword = current_keyword
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Expectet: {self.key_word} Passed: {self.current_keyword} Msg:{self.message}'


class WrongeData(Exception):
    """
    WrongeData Data is not Correct

    Args:
        Exception ([type]): Main Class for exceptions
    """

    def __init__(self, data: str, message: str = ""):
        self.data = data
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Passed Data: {self.data} Msg:{self.message}'