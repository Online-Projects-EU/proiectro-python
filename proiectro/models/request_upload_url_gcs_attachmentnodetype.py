from enum import Enum


class RequestUploadUrlGCSAttachmentnodetype(str, Enum):
    EXTERNAL_SUPPORT_REQUEST = "external_support_request"
    INTERNAL_SUPPORT_REQUEST = "internal_support_request"
    MEMBER = "member"
    OPERATIONAL_WORK_ITEM = "operational_work_item"
    ORG = "org"
    ORG_BRANDING = "org_branding"
    PAYMENT_COMMENT = "payment_comment"
    PRODUCT_COMMENT = "product_comment"
    PROJECT_COMMENT = "project_comment"
    PROJECT_WORK_ITEM = "project_work_item"
    PROPOSAL = "proposal"
    RESOURCE = "resource"
    RFP = "rfp"
    SUPPORT_REQUEST_COMMENT = "support_request_comment"
    TENANT = "tenant"
    USER = "user"
    WORK_ITEM_COMMENT = "work_item_comment"

    def __str__(self) -> str:
        return str(self.value)
