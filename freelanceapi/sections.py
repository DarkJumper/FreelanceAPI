from abc import ABC, abstractmethod


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
