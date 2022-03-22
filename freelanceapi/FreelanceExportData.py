from abc import ABC, abstractmethod

from .sections.sections import csv_sections


class FreelanceExportData(ABC):

    def __init__(self, file_data: tuple[str] = tuple()) -> None:
        self._data = file_data

    @abstractmethod
    def complete_file(self) -> tuple[tuple]:
        pass

    def extract_sections(self, section: str) -> tuple[tuple]:
        begin_key, end_key = csv_sections(section)
        search_dict = {}
        search_count = 0
        for line in range(len(self._data)):
            if begin_key in self._data[line]:
                search_dict[search_count] = [line]
            if end_key in self._data[line]:
                search_dict[search_count].append(line)
                search_count += 1
        section_list = [self._data[value[0]:value[1]] for value in search_dict.values()]
        return tuple(section_list)


class FreelancePlcData(FreelanceExportData):
    pass


class FreelancePleData(FreelanceExportData):
    pass


class FreelanceCsvData(FreelanceExportData):

    def complete_file(self) -> tuple[tuple]:
        return tuple(tuple(row.split(";")) for row in self._data)
