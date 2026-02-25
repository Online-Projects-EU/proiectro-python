from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EditSubtenant")


@_attrs_define
class EditSubtenant:
    """
    Attributes:
        name (str):
        timezone (str):
        default_currency (str):
        country (str):
        manager (str):
    """

    name: str
    timezone: str
    default_currency: str
    country: str
    manager: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timezone = self.timezone

        default_currency = self.default_currency

        country = self.country

        manager = self.manager

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timezone": timezone,
                "default_currency": default_currency,
                "country": country,
                "manager": manager,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        timezone = d.pop("timezone")

        default_currency = d.pop("default_currency")

        country = d.pop("country")

        manager = d.pop("manager")

        edit_subtenant = cls(
            name=name,
            timezone=timezone,
            default_currency=default_currency,
            country=country,
            manager=manager,
        )

        edit_subtenant.additional_properties = d
        return edit_subtenant

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
