from enum import Enum


class PartnerPortalFileNamesNodeType(str, Enum):
    EXTERNAL_SUPPORT_REQUEST = "external_support_request"
    INTERNAL_SUPPORT_REQUEST = "internal_support_request"
    OPERATIONAL_WORK_ITEM = "operational_work_item"
    ORG = "org"
    PROJECT_WORK_ITEM = "project_work_item"
    PROPOSAL = "proposal"
    RESOURCE = "resource"
    RFP = "rfp"

    def __str__(self) -> str:
        return str(self.value)
