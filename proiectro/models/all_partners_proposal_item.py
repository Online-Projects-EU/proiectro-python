from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AllPartnersProposalItem")


@_attrs_define
class AllPartnersProposalItem:
    """Proposal item with partner context for aggregated view

    Attributes:
        id (str):
        title (str):
        description (None | str):
        status (str):
        created_at (str):
        estimated_value (None | str):
        currency (None | str):
        partner_tenant_name (str):
        proxy_subtenant_id (str):
        bridge_id (str):
    """

    id: str
    title: str
    description: None | str
    status: str
    created_at: str
    estimated_value: None | str
    currency: None | str
    partner_tenant_name: str
    proxy_subtenant_id: str
    bridge_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description: None | str
        description = self.description

        status = self.status

        created_at = self.created_at

        estimated_value: None | str
        estimated_value = self.estimated_value

        currency: None | str
        currency = self.currency

        partner_tenant_name = self.partner_tenant_name

        proxy_subtenant_id = self.proxy_subtenant_id

        bridge_id = self.bridge_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "status": status,
                "created_at": created_at,
                "estimated_value": estimated_value,
                "currency": currency,
                "partner_tenant_name": partner_tenant_name,
                "proxy_subtenant_id": proxy_subtenant_id,
                "bridge_id": bridge_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        status = d.pop("status")

        created_at = d.pop("created_at")

        def _parse_estimated_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        estimated_value = _parse_estimated_value(d.pop("estimated_value"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        partner_tenant_name = d.pop("partner_tenant_name")

        proxy_subtenant_id = d.pop("proxy_subtenant_id")

        bridge_id = d.pop("bridge_id")

        all_partners_proposal_item = cls(
            id=id,
            title=title,
            description=description,
            status=status,
            created_at=created_at,
            estimated_value=estimated_value,
            currency=currency,
            partner_tenant_name=partner_tenant_name,
            proxy_subtenant_id=proxy_subtenant_id,
            bridge_id=bridge_id,
        )

        all_partners_proposal_item.additional_properties = d
        return all_partners_proposal_item

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
