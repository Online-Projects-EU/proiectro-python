from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerAssetTicketItem")


@_attrs_define
class CustomerAssetTicketItem:
    """A support request linked to a customer asset

    Attributes:
        id (str):
        public_reference (str):
        title (str):
        status_name (str):
        status_lifecycle (str):
        type_name (str):
        severity_name (str):
        link_type (str):
        is_external (bool):
        updated_formatted (str):
        customer_name (None | str | Unset):
    """

    id: str
    public_reference: str
    title: str
    status_name: str
    status_lifecycle: str
    type_name: str
    severity_name: str
    link_type: str
    is_external: bool
    updated_formatted: str
    customer_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_reference = self.public_reference

        title = self.title

        status_name = self.status_name

        status_lifecycle = self.status_lifecycle

        type_name = self.type_name

        severity_name = self.severity_name

        link_type = self.link_type

        is_external = self.is_external

        updated_formatted = self.updated_formatted

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "public_reference": public_reference,
                "title": title,
                "status_name": status_name,
                "status_lifecycle": status_lifecycle,
                "type_name": type_name,
                "severity_name": severity_name,
                "link_type": link_type,
                "is_external": is_external,
                "updated_formatted": updated_formatted,
            }
        )
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        public_reference = d.pop("public_reference")

        title = d.pop("title")

        status_name = d.pop("status_name")

        status_lifecycle = d.pop("status_lifecycle")

        type_name = d.pop("type_name")

        severity_name = d.pop("severity_name")

        link_type = d.pop("link_type")

        is_external = d.pop("is_external")

        updated_formatted = d.pop("updated_formatted")

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        customer_asset_ticket_item = cls(
            id=id,
            public_reference=public_reference,
            title=title,
            status_name=status_name,
            status_lifecycle=status_lifecycle,
            type_name=type_name,
            severity_name=severity_name,
            link_type=link_type,
            is_external=is_external,
            updated_formatted=updated_formatted,
            customer_name=customer_name,
        )

        customer_asset_ticket_item.additional_properties = d
        return customer_asset_ticket_item

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
