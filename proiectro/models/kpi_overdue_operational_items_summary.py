from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIOverdueOperationalItemsSummary")



@_attrs_define
class KPIOverdueOperationalItemsSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            count (str | Unset):  Default: '0'.
            critical_count (str | Unset):  Default: '0'.
            high_count (str | Unset):  Default: '0'.
            oldest_days_overdue (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    count: str | Unset = '0'
    critical_count: str | Unset = '0'
    high_count: str | Unset = '0'
    oldest_days_overdue: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        critical_count = self.critical_count

        high_count = self.high_count

        oldest_days_overdue = self.oldest_days_overdue


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
        if high_count is not UNSET:
            field_dict["highCount"] = high_count
        if oldest_days_overdue is not UNSET:
            field_dict["oldestDaysOverdue"] = oldest_days_overdue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        critical_count = d.pop("criticalCount", UNSET)

        high_count = d.pop("highCount", UNSET)

        oldest_days_overdue = d.pop("oldestDaysOverdue", UNSET)

        kpi_overdue_operational_items_summary = cls(
            description=description,
            count=count,
            critical_count=critical_count,
            high_count=high_count,
            oldest_days_overdue=oldest_days_overdue,
        )


        kpi_overdue_operational_items_summary.additional_properties = d
        return kpi_overdue_operational_items_summary

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
