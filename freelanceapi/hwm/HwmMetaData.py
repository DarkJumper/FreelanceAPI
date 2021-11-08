from abc import ABC, abstractproperty


class HwmMetaData(ABC):

    @abstractproperty
    def get_keys(self):
        pass

    @abstractproperty
    def get_expected_key(self):
        pass
