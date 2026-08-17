from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIStaleOperationalItemsSummary")



@_attrs_define
class KPIStaleOperationalItemsSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            count (str | Unset):  Default: '0'.
            critical_count (str | Unset):  Default: '0'.
            oldest_days (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    count: str | Unset = '0'
    critical_count: str | Unset = '0'
    oldest_days: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        critical_count = self.critical_count

        oldest_days = self.oldest_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if critical_count is not UNSET:
            field_dict["criticalCount"] = critical_count
        if oldest_days is not UNSET:
            field_dict["oldestDays"] = oldest_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        critical_count = d.pop("criticalCount", UNSET)

        oldest_days = d.pop("oldestDays", UNSET)

        kpi_stale_operational_items_summary = cls(
            description=description,
            count=count,
            critical_count=critical_count,
            oldest_days=oldest_days,
        )


        kpi_stale_operational_items_summary.additional_properties = d
        return kpi_stale_operational_items_summary

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
