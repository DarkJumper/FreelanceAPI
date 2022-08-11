import re

from pydantic import validator


class Identifcation(str):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_ID

    @classmethod
    def validate_ID(cls, v: str) -> str:
        print(v)
        return v


class LengthDataset(int):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_LEN

    @classmethod
    def validate_LEN(cls, v: int) -> int:
        print(v)
        return v


class NextElementAvailable(int):

    _nextelement_numbers = [0, 1]

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_NA

    @classmethod
    def validate_NA(cls, na: str | int) -> int:
        if int(na) in cls._nextelement_numbers:
            return int(na)
        raise ValueError(f'Value passed is not correct! Available values -> {cls._nextelement_numbers}')


class MeasuringPoint():

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_MP

    @classmethod
    def validate_MP(cls, mp: str) -> str:
        if re.search("""[!\"#$%&'()*+,./:;<=>?@[\]^`{|}~]""", mp):
            raise ValueError('Value contains characters that are not allowed')
        if len(mp) > 12:
            raise ValueError('Value ist to long max. len 10')
        if not re.search("^[a-zA-Z_]", mp):
            raise ValueError('There is no character in the first place of the string')
        return mp


class ModuleType(str):

    _module_typs = ["M_BIN", "M_ANA"]

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_MT

    @classmethod
    def validate_MT(cls, mt: str) -> str:
        if mt in cls._module_typs:
            return mt
        raise ValueError(f'Module type does not exist! Available modules -> {cls._module_typs}')


class ShortText(str):

    _max_len: int = 12

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_ST

    @classmethod
    def validate_ST(cls, st: str) -> str:
        if len(st) > cls._max_len:
            raise ValueError(f'Value ist to long max. len {cls._max_len}')
        return st


class LongText(str):

    _max_len: int = 12

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_LT

    @classmethod
    def validate_LT(cls, lt: str) -> str:
        if len(lt) > 30:
            raise ValueError(f'Value ist to long max. len {cls._max_len}')
        return lt


class AreaDefinition(int):

    _area_numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_AD

    @classmethod
    def validate_AD(cls, ad: str | int) -> int:
        if int(ad) in cls._area_numbers:
            return int(ad)
        raise ValueError(f'Area Number is invalid! valid ->{cls._area_numbers}')


class StatusBit(int):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_SB

    @classmethod
    def validate_SB(cls, v: int) -> int:
        print(v)
        return v


class VariableName(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_VN

    @classmethod
    def validate_VN(cls, v: str) -> str:
        print(v)
        return v


class DataTyp(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_DT

    @classmethod
    def validate_DT(cls, v: str) -> str:
        print(v)
        return v


class VariableText(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_VT

    @classmethod
    def validate_VT(cls, v: str) -> str:
        print(v)
        return v


class ProcessImage(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_PI

    @classmethod
    def validate_PI(cls, v: str) -> str:
        print(v)
        return v


class ExportedVariable(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_EV

    @classmethod
    def validate_EV(cls, v: str) -> str:
        print(v)
        return v


class VariableOrConst(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_VC

    @classmethod
    def validate_VC(cls, v: str) -> str:
        print(v)
        return v


class Fbs(str):

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_FB

    @classmethod
    def validate_FB(cls, v: str) -> str:
        print(v)
        return v


class Libary:

    @classmethod
    def __get_validators__(cls) -> None:
        yield cls.validate_LB

    @classmethod
    def validate_LB(cls, v: str) -> str:
        print(v)
        return v


class DtmNumber():
    pass


class DtmConfig():
    pass


class QuantityCounter():
    pass


class FunctionName():
    pass


class ChannelName():
    pass


class InputOutput():
    pass


class UsedByte():
    pass


class Bit():
    pass


class ByteLength():
    pass


class Commend():
    pass


class AreaChar():
    pass


class LengthAreaText():
    pass


class AreaName():
    pass


class ParaSettings():
    pass


class NoIdear():
    pass
