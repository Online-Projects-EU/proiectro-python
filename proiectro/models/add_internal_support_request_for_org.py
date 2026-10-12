from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddInternalSupportRequestForOrg")


@_attrs_define
class AddInternalSupportRequestForOrg:
    """Input schema for creating internal support request for a specific organization

    Attributes:
        request_type (str):
        request_severity (str):
        title (str):
        description (str):
        customer_id (str):
    """

    request_type: str
    request_severity: str
    title: str
    description: str
    customer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_type = self.request_type

        request_severity = self.request_severity

        title = self.title

        description = self.description

        customer_id = self.customer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_type": request_type,
                "request_severity": request_severity,
                "title": title,
                "description": description,
                "customer_id": customer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_type = d.pop("request_type")

        request_severity = d.pop("request_severity")

        title = d.pop("title")

        description = d.pop("description")

        customer_id = d.pop("customer_id")

        add_internal_support_request_for_org = cls(
            request_type=request_type,
            request_severity=request_severity,
            title=title,
            description=description,
            customer_id=customer_id,
        )

        add_internal_support_request_for_org.additional_properties = d
        return add_internal_support_request_for_org

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
