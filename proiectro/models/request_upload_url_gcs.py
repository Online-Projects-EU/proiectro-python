from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_upload_url_gcs_attachmentnodetype import (
    RequestUploadUrlGCSAttachmentnodetype,
)

T = TypeVar("T", bound="RequestUploadUrlGCS")


@_attrs_define
class RequestUploadUrlGCS:
    """
    Attributes:
        file_name (str):
        file_size (int):
        content_type (str):
        attachment_node_type (RequestUploadUrlGCSAttachmentnodetype):
        attachment_node_id (str):
    """

    file_name: str
    file_size: int
    content_type: str
    attachment_node_type: RequestUploadUrlGCSAttachmentnodetype
    attachment_node_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        file_size = self.file_size

        content_type = self.content_type

        attachment_node_type = self.attachment_node_type.value

        attachment_node_id = self.attachment_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "fileSize": file_size,
                "contentType": content_type,
                "attachmentNodeType": attachment_node_type,
                "attachmentNodeId": attachment_node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        file_size = d.pop("fileSize")

        content_type = d.pop("contentType")

        attachment_node_type = RequestUploadUrlGCSAttachmentnodetype(
            d.pop("attachmentNodeType")
        )

        attachment_node_id = d.pop("attachmentNodeId")

        request_upload_url_gcs = cls(
            file_name=file_name,
            file_size=file_size,
            content_type=content_type,
            attachment_node_type=attachment_node_type,
            attachment_node_id=attachment_node_id,
        )

        request_upload_url_gcs.additional_properties = d
        return request_upload_url_gcs

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
