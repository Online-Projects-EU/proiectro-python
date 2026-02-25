from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyTicketItem")


@_attrs_define
class MyTicketItem:
    """Individual support ticket for cross-tenant My Tickets view

    Attributes:
        id (str):
        public_reference (str):
        title (str):
        status_name (str):
        status_lifecycle (str):
        tenant_name (str):
        tenant_path (str):
        ticket_type (str):
        url (str):
        severity_name (None | str | Unset):
        severity_score (int | None | Unset):
        customer_name (None | str | Unset):
    """

    id: str
    public_reference: str
    title: str
    status_name: str
    status_lifecycle: str
    tenant_name: str
    tenant_path: str
    ticket_type: str
    url: str
    severity_name: None | str | Unset = UNSET
    severity_score: int | None | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_reference = self.public_reference

        title = self.title

        status_name = self.status_name

        status_lifecycle = self.status_lifecycle

        tenant_name = self.tenant_name

        tenant_path = self.tenant_path

        ticket_type = self.ticket_type

        url = self.url

        severity_name: None | str | Unset
        if isinstance(self.severity_name, Unset):
            severity_name = UNSET
        else:
            severity_name = self.severity_name

        severity_score: int | None | Unset
        if isinstance(self.severity_score, Unset):
            severity_score = UNSET
        else:
            severity_score = self.severity_score

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
                "tenant_name": tenant_name,
                "tenant_path": tenant_path,
                "ticket_type": ticket_type,
                "url": url,
            }
        )
        if severity_name is not UNSET:
            field_dict["severity_name"] = severity_name
        if severity_score is not UNSET:
            field_dict["severity_score"] = severity_score
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

        tenant_name = d.pop("tenant_name")

        tenant_path = d.pop("tenant_path")

        ticket_type = d.pop("ticket_type")

        url = d.pop("url")

        def _parse_severity_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity_name = _parse_severity_name(d.pop("severity_name", UNSET))

        def _parse_severity_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        severity_score = _parse_severity_score(d.pop("severity_score", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        my_ticket_item = cls(
            id=id,
            public_reference=public_reference,
            title=title,
            status_name=status_name,
            status_lifecycle=status_lifecycle,
            tenant_name=tenant_name,
            tenant_path=tenant_path,
            ticket_type=ticket_type,
            url=url,
            severity_name=severity_name,
            severity_score=severity_score,
            customer_name=customer_name,
        )

        my_ticket_item.additional_properties = d
        return my_ticket_item

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
