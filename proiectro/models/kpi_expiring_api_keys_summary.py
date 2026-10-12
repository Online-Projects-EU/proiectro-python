from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KPIExpiringApiKeysSummary")


@_attrs_define
class KPIExpiringApiKeysSummary:
    """
    Attributes:
        description (str | Unset):  Default: ''.
        count (str | Unset):  Default: '0'.
        expiring_today (str | Unset):  Default: '0'.
    """

    description: str | Unset = ""
    count: str | Unset = "0"
    expiring_today: str | Unset = "0"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        expiring_today = self.expiring_today

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if expiring_today is not UNSET:
            field_dict["expiringToday"] = expiring_today

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        expiring_today = d.pop("expiringToday", UNSET)

        kpi_expiring_api_keys_summary = cls(
            description=description,
            count=count,
            expiring_today=expiring_today,
        )

        kpi_expiring_api_keys_summary.additional_properties = d
        return kpi_expiring_api_keys_summary

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
