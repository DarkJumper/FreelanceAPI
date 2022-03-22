import io
from contextlib import contextmanager

from ._FreelanceFactories import ExportedFreelanceFactories
from .sections.sections import Section


@contextmanager
def read_export_file(file_name: str, file_suffix: str) -> tuple[str]:
    """
    read_export_file [Freelance export file is read and output as tuple.
    The file extension of the export file must be specified to ensure that the correct form can be returned.]

    Args:
        file_name (str): [path of the file]
        file_suffix (str): [ending of the file to be read]

    Raises:
        AttributeError: [File type cannot be read]

    Yields:
        Iterator[tuple[str]]: [Filedata are summarized in tuples]
    """
    if file_suffix.lower() != "csv":
        raise AttributeError(f'{file_suffix} is not supported')
    TextWrapper = open(file_name, "r", newline='', encoding='utf-16')
    try:
        yield tuple(row.strip() for row in TextWrapper)
    finally:
        TextWrapper.close()


def evaluate_row(listed_data: str, sep: str = ";") -> tuple[dict, str]:
    """
    evaluate_row Matching instances to the key word are searched for and returned accordingly.

    Args:
        listed_data (str): An exported row of freelance is required. These must contain a key word. Key words are predefined.
        sep (str, optional): Seperator for the string must be set. Defaults to ";".


    Raises:
        KeyError: If the keyword in the string does not match the expected string, the error is returned.

    Returns:
        tuple: a tuple with an instance to convert to a dict and to convert to string
    """
    key_word, *_ = listed_data.split(sep)
    find_msr_factory_tuple = ExportedFreelanceFactories()
    if key_word not in find_msr_factory_tuple.keys():
        raise KeyError(f"unknown keyword in line: {key_word}.")
    (dict_class, string_class) = find_msr_factory_tuple[key_word]
    return (dict_class(), string_class())


def get_sections(file_data: read_export_file, section: Section) -> tuple[tuple[str]]:
    """
    get_sections [The different areas in the export file are searched for and output.]

    Args:
        file_data (read_export_file): [the data evaluated by the context manager must be transferred.]
        section (Section): [The desired subrange from the export file must be specified.]

    Returns:
        tuple[tuple[str]]: [The selected part will be output from the file.It is always a tuple within a tuple. So that all data is passed even if the section occurs more often in the file.]
    """
    list_of_sections = []
    found_key = False
    section_list = []
    for element in file_data:
        if found_key:
            section_list.append(element)
        if section().get_begin_of_section() in element:
            found_key = True
            section_list = [element]
        if section().get_end_of_section() in element:
            list_of_sections.append(tuple(section_list))
            found_key = False
    return tuple(list_of_sections)
