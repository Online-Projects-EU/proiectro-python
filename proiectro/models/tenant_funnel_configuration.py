from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantFunnelConfiguration")


@_attrs_define
class TenantFunnelConfiguration:
    """
    Attributes:
        id (str):
        name (str):
        is_active (bool):
        description (str):
        used_for_quote_requests (bool | Unset):  Default: False.
        used_for_orders (bool | Unset):  Default: False.
    """

    id: str
    name: str
    is_active: bool
    description: str
    used_for_quote_requests: bool | Unset = False
    used_for_orders: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_active = self.is_active

        description = self.description

        used_for_quote_requests = self.used_for_quote_requests

        used_for_orders = self.used_for_orders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_active": is_active,
                "description": description,
            }
        )
        if used_for_quote_requests is not UNSET:
            field_dict["used_for_quote_requests"] = used_for_quote_requests
        if used_for_orders is not UNSET:
            field_dict["used_for_orders"] = used_for_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_active = d.pop("is_active")

        description = d.pop("description")

        used_for_quote_requests = d.pop("used_for_quote_requests", UNSET)

        used_for_orders = d.pop("used_for_orders", UNSET)

        tenant_funnel_configuration = cls(
            id=id,
            name=name,
            is_active=is_active,
            description=description,
            used_for_quote_requests=used_for_quote_requests,
            used_for_orders=used_for_orders,
        )

        tenant_funnel_configuration.additional_properties = d
        return tenant_funnel_configuration

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
