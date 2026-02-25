from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenant")


@_attrs_define
class EditTenant:
    """
    Attributes:
        name (str):
        timezone (str):
        default_currency (str):
        country (str):
        minimum_acceptable_margin (float | str):
        bridge_requests_allowed (bool | None | Unset):  Default: False.
    """

    name: str
    timezone: str
    default_currency: str
    country: str
    minimum_acceptable_margin: float | str
    bridge_requests_allowed: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timezone = self.timezone

        default_currency = self.default_currency

        country = self.country

        minimum_acceptable_margin: float | str
        minimum_acceptable_margin = self.minimum_acceptable_margin

        bridge_requests_allowed: bool | None | Unset
        if isinstance(self.bridge_requests_allowed, Unset):
            bridge_requests_allowed = UNSET
        else:
            bridge_requests_allowed = self.bridge_requests_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timezone": timezone,
                "default_currency": default_currency,
                "country": country,
                "minimum_acceptable_margin": minimum_acceptable_margin,
            }
        )
        if bridge_requests_allowed is not UNSET:
            field_dict["bridge_requests_allowed"] = bridge_requests_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        timezone = d.pop("timezone")

        default_currency = d.pop("default_currency")

        country = d.pop("country")

        def _parse_minimum_acceptable_margin(data: object) -> float | str:
            return cast(float | str, data)

        minimum_acceptable_margin = _parse_minimum_acceptable_margin(
            d.pop("minimum_acceptable_margin")
        )

        def _parse_bridge_requests_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        bridge_requests_allowed = _parse_bridge_requests_allowed(
            d.pop("bridge_requests_allowed", UNSET)
        )

        edit_tenant = cls(
            name=name,
            timezone=timezone,
            default_currency=default_currency,
            country=country,
            minimum_acceptable_margin=minimum_acceptable_margin,
            bridge_requests_allowed=bridge_requests_allowed,
        )

        edit_tenant.additional_properties = d
        return edit_tenant

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
