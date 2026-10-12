from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditFunnelConfiguration")


@_attrs_define
class EditFunnelConfiguration:
    """
    Attributes:
        name (str):
        is_active (bool | None | Unset):
        description (None | str | Unset):
        used_for_quote_requests (bool | None | Unset):
        used_for_orders (bool | None | Unset):
    """

    name: str
    is_active: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    used_for_quote_requests: bool | None | Unset = UNSET
    used_for_orders: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        used_for_quote_requests: bool | None | Unset
        if isinstance(self.used_for_quote_requests, Unset):
            used_for_quote_requests = UNSET
        else:
            used_for_quote_requests = self.used_for_quote_requests

        used_for_orders: bool | None | Unset
        if isinstance(self.used_for_orders, Unset):
            used_for_orders = UNSET
        else:
            used_for_orders = self.used_for_orders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if description is not UNSET:
            field_dict["description"] = description
        if used_for_quote_requests is not UNSET:
            field_dict["used_for_quote_requests"] = used_for_quote_requests
        if used_for_orders is not UNSET:
            field_dict["used_for_orders"] = used_for_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_used_for_quote_requests(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        used_for_quote_requests = _parse_used_for_quote_requests(
            d.pop("used_for_quote_requests", UNSET)
        )

        def _parse_used_for_orders(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        used_for_orders = _parse_used_for_orders(d.pop("used_for_orders", UNSET))

        edit_funnel_configuration = cls(
            name=name,
            is_active=is_active,
            description=description,
            used_for_quote_requests=used_for_quote_requests,
            used_for_orders=used_for_orders,
        )

        edit_funnel_configuration.additional_properties = d
        return edit_funnel_configuration

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
