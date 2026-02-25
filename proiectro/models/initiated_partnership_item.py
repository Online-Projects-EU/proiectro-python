from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InitiatedPartnershipItem")


@_attrs_define
class InitiatedPartnershipItem:
    """Single initiated partnership item

    Attributes:
        bridge_id (str):
        subtenant_id (str):
        subtenant_name (str):
        partner_tenant_name (str):
        expires_at (None | str | Unset):
    """

    bridge_id: str
    subtenant_id: str
    subtenant_name: str
    partner_tenant_name: str
    expires_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        subtenant_id = self.subtenant_id

        subtenant_name = self.subtenant_name

        partner_tenant_name = self.partner_tenant_name

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "subtenant_id": subtenant_id,
                "subtenant_name": subtenant_name,
                "partner_tenant_name": partner_tenant_name,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        subtenant_id = d.pop("subtenant_id")

        subtenant_name = d.pop("subtenant_name")

        partner_tenant_name = d.pop("partner_tenant_name")

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        initiated_partnership_item = cls(
            bridge_id=bridge_id,
            subtenant_id=subtenant_id,
            subtenant_name=subtenant_name,
            partner_tenant_name=partner_tenant_name,
            expires_at=expires_at,
        )

        initiated_partnership_item.additional_properties = d
        return initiated_partnership_item

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
