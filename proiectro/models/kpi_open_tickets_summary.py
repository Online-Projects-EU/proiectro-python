from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIOpenTicketsSummary")



@_attrs_define
class KPIOpenTicketsSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            count (str | Unset):  Default: '0'.
            high_severity_count (str | Unset):  Default: '0'.
            unassigned_count (str | Unset):  Default: '0'.
            oldest_hours (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    count: str | Unset = '0'
    high_severity_count: str | Unset = '0'
    unassigned_count: str | Unset = '0'
    oldest_hours: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        high_severity_count = self.high_severity_count

        unassigned_count = self.unassigned_count

        oldest_hours = self.oldest_hours


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if high_severity_count is not UNSET:
            field_dict["highSeverityCount"] = high_severity_count
        if unassigned_count is not UNSET:
            field_dict["unassignedCount"] = unassigned_count
        if oldest_hours is not UNSET:
            field_dict["oldestHours"] = oldest_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        high_severity_count = d.pop("highSeverityCount", UNSET)

        unassigned_count = d.pop("unassignedCount", UNSET)

        oldest_hours = d.pop("oldestHours", UNSET)

        kpi_open_tickets_summary = cls(
            description=description,
            count=count,
            high_severity_count=high_severity_count,
            unassigned_count=unassigned_count,
            oldest_hours=oldest_hours,
        )


        kpi_open_tickets_summary.additional_properties = d
        return kpi_open_tickets_summary

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
