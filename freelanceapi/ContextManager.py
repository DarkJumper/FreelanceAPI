import os

from .FreelanceExportData import (FreelanceCsvData, FreelanceExportData, FreelancePlcData, FreelancePleData)


class FreelanceReader:
    """
    Freelane API Context Manager 
    """

    def __init__(self, file_name: str) -> None:
        filename, self.file_extension = os.path.splitext(file_name)
        if self.file_extension.lower() != ".csv":
            raise AttributeError(f'{self.file_extension} is not supported with this Context Manager!')
        self._wrapper = open(file_name, "r", newline="", encoding='utf-16')

    def __enter__(self) -> FreelanceExportData:
        if self.file_extension.lower() == ".csv":
            return FreelanceCsvData(tuple(row.strip() for row in self._wrapper))
        raise AttributeError(f'{self.file_extension} is currently not supported')

    def __exit__(self, error: Exception, value: object, traceback: object) -> None:
        self._wrapper.close()
