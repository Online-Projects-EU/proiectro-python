from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPITeamWorkloadSummary")



@_attrs_define
class KPITeamWorkloadSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            member_count (str | Unset):  Default: '0'.
            overloaded_count (str | Unset):  Default: '0'.
            total_active_items (str | Unset):  Default: '0'.
            avg_items_per_member (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    member_count: str | Unset = '0'
    overloaded_count: str | Unset = '0'
    total_active_items: str | Unset = '0'
    avg_items_per_member: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        member_count = self.member_count

        overloaded_count = self.overloaded_count

        total_active_items = self.total_active_items

        avg_items_per_member = self.avg_items_per_member


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if overloaded_count is not UNSET:
            field_dict["overloadedCount"] = overloaded_count
        if total_active_items is not UNSET:
            field_dict["totalActiveItems"] = total_active_items
        if avg_items_per_member is not UNSET:
            field_dict["avgItemsPerMember"] = avg_items_per_member

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        member_count = d.pop("memberCount", UNSET)

        overloaded_count = d.pop("overloadedCount", UNSET)

        total_active_items = d.pop("totalActiveItems", UNSET)

        avg_items_per_member = d.pop("avgItemsPerMember", UNSET)

        kpi_team_workload_summary = cls(
            description=description,
            member_count=member_count,
            overloaded_count=overloaded_count,
            total_active_items=total_active_items,
            avg_items_per_member=avg_items_per_member,
        )


        kpi_team_workload_summary.additional_properties = d
        return kpi_team_workload_summary

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
