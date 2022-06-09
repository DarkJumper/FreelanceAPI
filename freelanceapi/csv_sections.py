from abc import ABC, abstractmethod

from .FreelanceExportData import FreelanceReader


class Section(ABC):

    @abstractmethod
    def get_begin_of_section(self) -> str:
        pass

    @abstractmethod
    def get_end_of_section(self) -> str:
        pass


class Pbaum(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_PBAUMSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_PBAUMSECTION]"


class Node(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_NODESECTION]"

    def get_end_of_section(self) -> str:
        return "[END_NODESECTION]"


class EAM(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_EAMSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_EAMSECTION]"


class EAMInit(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_EAMINITSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_EAMINITSECTION]"


class OPCAdress(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_OPCADDRESSSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_OPCADDRESSSECTION]"


class MSR(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_MSRSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_MSRSECTION]"


class HD(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_HDSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_HDSECTION]"


class HDTextList(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_HDTEXTLISTSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_HDTEXTLISTSECTION]"


class Conn(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_CONNSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_CONNSECTION]"


class OPCConn(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_OPCCONNSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_OPCCONNSECTION]"


class HW2(Section):

    def get_begin_of_section(self) -> str:
        return "HW2_CHECK_BEGIN"

    def get_end_of_section(self) -> str:
        return "HW2_CHECK_END"


class HardWareManager(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_HARDWAREMANAGER]"

    def get_end_of_section(self) -> str:
        return "[END_HARDWAREMANAGER]"


class ResourceAssociation(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_RESOURCEASSOCIATIONSECTION]"

    def get_end_of_section(self) -> str:
        return "[END_RESOURCEASSOCIATIONSECTION]"


class ProjectHeader(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_PROJECTHEADER]"

    def get_end_of_section(self) -> str:
        return "[END_PROJECTHEADER]"


class AreaDefinition(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_AREADEFINITION]"

    def get_end_of_section(self) -> str:
        return "[END_AREADEFINITION]"


class ProjectComment(Section):

    def get_begin_of_section(self) -> str:
        return "[BEGIN_PROJECTCOMMENT]"

    def get_end_of_section(self) -> str:
        return "[END_PROJECTCOMMENT]"


_CSV_SECTION_FACTORY = {
    "Project Comment": ProjectComment,
    "Node": Node,
    "HW2": HW2,
    "Area": AreaDefinition,
    "Header": ProjectHeader,
    "Resorce Association": ResourceAssociation,
    "Hardware Manager": HardWareManager,
    "Hardware": HW2,
    "OPC Connection": OPCConn,
    "Connections": Conn,
    "HD Text": HDTextList,
    "HD": HD,
    "MSR": MSR,
    "OPC Adressing": OPCAdress,
    "EAM Initialisation": EAMInit,
    "EAM": EAM,
    "Project Tree": Pbaum,
    }


def csv_sections(section: str) -> tuple[str, str]:
    if section not in _CSV_SECTION_FACTORY.keys():
        raise KeyError(f"unknown section: {section}.")
    section_class = _CSV_SECTION_FACTORY[section]()
    return (section_class.get_begin_of_section(), section_class.get_end_of_section())


def get_sections(file_data: FreelanceReader, section: Section) -> tuple[tuple[str]]:
    """
    get_sections [The different areas in the export file are searched for and output.]

    Args:
        file_data (FreelanceReader): [the data evaluated by the context manager must be transferred.]
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
