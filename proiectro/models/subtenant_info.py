from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubtenantInfo")


@_attrs_define
class SubtenantInfo:
    """
    Attributes:
        name (str):
        timezone (str):
        default_currency (None | str | Unset):
        country (None | str | Unset):
        manager_name (None | str | Unset):
        local_time (None | str | Unset):
    """

    name: str
    timezone: str
    default_currency: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    manager_name: None | str | Unset = UNSET
    local_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timezone = self.timezone

        default_currency: None | str | Unset
        if isinstance(self.default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = self.default_currency

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        manager_name: None | str | Unset
        if isinstance(self.manager_name, Unset):
            manager_name = UNSET
        else:
            manager_name = self.manager_name

        local_time: None | str | Unset
        if isinstance(self.local_time, Unset):
            local_time = UNSET
        else:
            local_time = self.local_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timezone": timezone,
            }
        )
        if default_currency is not UNSET:
            field_dict["default_currency"] = default_currency
        if country is not UNSET:
            field_dict["country"] = country
        if manager_name is not UNSET:
            field_dict["manager_name"] = manager_name
        if local_time is not UNSET:
            field_dict["local_time"] = local_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        timezone = d.pop("timezone")

        def _parse_default_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_currency = _parse_default_currency(d.pop("default_currency", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_manager_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manager_name = _parse_manager_name(d.pop("manager_name", UNSET))

        def _parse_local_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_time = _parse_local_time(d.pop("local_time", UNSET))

        subtenant_info = cls(
            name=name,
            timezone=timezone,
            default_currency=default_currency,
            country=country,
            manager_name=manager_name,
            local_time=local_time,
        )

        subtenant_info.additional_properties = d
        return subtenant_info

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
