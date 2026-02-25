from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EditExternalSupportRequest")


@_attrs_define
class EditExternalSupportRequest:
    """
    Attributes:
        title (str):
        description (str):
        request_type (str):
        request_severity (str):
    """

    title: str
    description: str
    request_type: str
    request_severity: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        request_type = self.request_type

        request_severity = self.request_severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "description": description,
                "request_type": request_type,
                "request_severity": request_severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description")

        request_type = d.pop("request_type")

        request_severity = d.pop("request_severity")

        edit_external_support_request = cls(
            title=title,
            description=description,
            request_type=request_type,
            request_severity=request_severity,
        )

        edit_external_support_request.additional_properties = d
        return edit_external_support_request

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
