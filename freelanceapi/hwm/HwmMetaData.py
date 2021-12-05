from abc import ABC, abstractproperty


class HwmMetaData(ABC):

    @abstractproperty
    def get_keys(self):
        pass

    @abstractproperty
    def get_expected_key(self):
        pass


class Hw2Blob(HwmMetaData):
    expected_key: str = "[HW2_BLOB]"
    keys: list[str] = ["KW", "DTMN", "QC", "DTMC"]

    @property
    def get_keys(self) -> str:
        return self.keys

    @property
    def get_expected_key(self) -> list[str]:
        return self.expected_key


class BeginIODescription(HwmMetaData):
    expected_key: str = "[BEGIN_IODESCRIPTION]"
    keys: list[str] = [
        "KW", "CN", "IO", "DT", "UB", "B", "BL", "VN", "C", "?1", "?2", "?3", "?4", "?5", "?6", "?7", "?8"
        ]

    @property
    def get_keys(self) -> str:
        return self.keys

    @property
    def get_expected_key(self) -> list[str]:
        return self.expected_key
