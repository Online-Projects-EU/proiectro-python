from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AddExternalSupportRequestForCustomer")



@_attrs_define
class AddExternalSupportRequestForCustomer:
    """ Input schema for creating an external support request on behalf of a customer.

        Attributes:
            requester_id (str):
            request_type (str):
            request_severity (str):
            title (str):
            description (str):
     """

    requester_id: str
    request_type: str
    request_severity: str
    title: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        requester_id = self.requester_id

        request_type = self.request_type

        request_severity = self.request_severity

        title = self.title

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "requester_id": requester_id,
            "request_type": request_type,
            "request_severity": request_severity,
            "title": title,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requester_id = d.pop("requester_id")

        request_type = d.pop("request_type")

        request_severity = d.pop("request_severity")

        title = d.pop("title")

        description = d.pop("description")

        add_external_support_request_for_customer = cls(
            requester_id=requester_id,
            request_type=request_type,
            request_severity=request_severity,
            title=title,
            description=description,
        )


        add_external_support_request_for_customer.additional_properties = d
        return add_external_support_request_for_customer

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
