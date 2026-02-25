from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddPartnerSupportRequest")


@_attrs_define
class AddPartnerSupportRequest:
    """Input schema for partner creating support request in supplier tenant

    Attributes:
        bridge_id (str):
        request_type (str):
        request_severity (str):
        title (str):
        description (str):
        project_id (None | str | Unset):
        product_id (None | str | Unset):
    """

    bridge_id: str
    request_type: str
    request_severity: str
    title: str
    description: str
    project_id: None | str | Unset = UNSET
    product_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        request_type = self.request_type

        request_severity = self.request_severity

        title = self.title

        description = self.description

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "request_type": request_type,
                "request_severity": request_severity,
                "title": title,
                "description": description,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        request_type = d.pop("request_type")

        request_severity = d.pop("request_severity")

        title = d.pop("title")

        description = d.pop("description")

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        add_partner_support_request = cls(
            bridge_id=bridge_id,
            request_type=request_type,
            request_severity=request_severity,
            title=title,
            description=description,
            project_id=project_id,
            product_id=product_id,
        )

        add_partner_support_request.additional_properties = d
        return add_partner_support_request

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
