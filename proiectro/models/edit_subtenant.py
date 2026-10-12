from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        domains (None | str | Unset):
        portal_ordering_enabled (bool | None | Unset):
        portal_quote_requests_enabled (bool | None | Unset):
    """

    name: str
    timezone: str
    default_currency: str
    country: str
    manager: str
    domains: None | str | Unset = UNSET
    portal_ordering_enabled: bool | None | Unset = UNSET
    portal_quote_requests_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timezone = self.timezone

        default_currency = self.default_currency

        country = self.country

        manager = self.manager

        domains: None | str | Unset
        if isinstance(self.domains, Unset):
            domains = UNSET
        else:
            domains = self.domains

        portal_ordering_enabled: bool | None | Unset
        if isinstance(self.portal_ordering_enabled, Unset):
            portal_ordering_enabled = UNSET
        else:
            portal_ordering_enabled = self.portal_ordering_enabled

        portal_quote_requests_enabled: bool | None | Unset
        if isinstance(self.portal_quote_requests_enabled, Unset):
            portal_quote_requests_enabled = UNSET
        else:
            portal_quote_requests_enabled = self.portal_quote_requests_enabled

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
        if domains is not UNSET:
            field_dict["domains"] = domains
        if portal_ordering_enabled is not UNSET:
            field_dict["portal_ordering_enabled"] = portal_ordering_enabled
        if portal_quote_requests_enabled is not UNSET:
            field_dict["portal_quote_requests_enabled"] = portal_quote_requests_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        timezone = d.pop("timezone")

        default_currency = d.pop("default_currency")

        country = d.pop("country")

        manager = d.pop("manager")

        def _parse_domains(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domains = _parse_domains(d.pop("domains", UNSET))

        def _parse_portal_ordering_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_ordering_enabled = _parse_portal_ordering_enabled(
            d.pop("portal_ordering_enabled", UNSET)
        )

        def _parse_portal_quote_requests_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_quote_requests_enabled = _parse_portal_quote_requests_enabled(
            d.pop("portal_quote_requests_enabled", UNSET)
        )

        edit_subtenant = cls(
            name=name,
            timezone=timezone,
            default_currency=default_currency,
            country=country,
            manager=manager,
            domains=domains,
            portal_ordering_enabled=portal_ordering_enabled,
            portal_quote_requests_enabled=portal_quote_requests_enabled,
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
