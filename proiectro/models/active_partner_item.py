from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivePartnerItem")


@_attrs_define
class ActivePartnerItem:
    """Single active partner item - partner subtenant names are never exposed for privacy

    Attributes:
        bridge_id (str):
        subtenant_id (str):
        subtenant_name (str):
        partner_tenant_name (str):
        partner_logo_url (str):
        status (str):
        established_at (None | str | Unset):
    """

    bridge_id: str
    subtenant_id: str
    subtenant_name: str
    partner_tenant_name: str
    partner_logo_url: str
    status: str
    established_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        subtenant_id = self.subtenant_id

        subtenant_name = self.subtenant_name

        partner_tenant_name = self.partner_tenant_name

        partner_logo_url = self.partner_logo_url

        status = self.status

        established_at: None | str | Unset
        if isinstance(self.established_at, Unset):
            established_at = UNSET
        else:
            established_at = self.established_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "subtenant_id": subtenant_id,
                "subtenant_name": subtenant_name,
                "partner_tenant_name": partner_tenant_name,
                "partner_logo_url": partner_logo_url,
                "status": status,
            }
        )
        if established_at is not UNSET:
            field_dict["established_at"] = established_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        subtenant_id = d.pop("subtenant_id")

        subtenant_name = d.pop("subtenant_name")

        partner_tenant_name = d.pop("partner_tenant_name")

        partner_logo_url = d.pop("partner_logo_url")

        status = d.pop("status")

        def _parse_established_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        established_at = _parse_established_at(d.pop("established_at", UNSET))

        active_partner_item = cls(
            bridge_id=bridge_id,
            subtenant_id=subtenant_id,
            subtenant_name=subtenant_name,
            partner_tenant_name=partner_tenant_name,
            partner_logo_url=partner_logo_url,
            status=status,
            established_at=established_at,
        )

        active_partner_item.additional_properties = d
        return active_partner_item

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
