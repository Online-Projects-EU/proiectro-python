from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KPIUnassignedItemsSummary")


@_attrs_define
class KPIUnassignedItemsSummary:
    """
    Attributes:
        description (str | Unset):  Default: ''.
        total_count (str | Unset):  Default: '0'.
        support_count (str | Unset):  Default: '0'.
        operations_count (str | Unset):  Default: '0'.
        work_count (str | Unset):  Default: '0'.
    """

    description: str | Unset = ""
    total_count: str | Unset = "0"
    support_count: str | Unset = "0"
    operations_count: str | Unset = "0"
    work_count: str | Unset = "0"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        total_count = self.total_count

        support_count = self.support_count

        operations_count = self.operations_count

        work_count = self.work_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if support_count is not UNSET:
            field_dict["supportCount"] = support_count
        if operations_count is not UNSET:
            field_dict["operationsCount"] = operations_count
        if work_count is not UNSET:
            field_dict["workCount"] = work_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        total_count = d.pop("totalCount", UNSET)

        support_count = d.pop("supportCount", UNSET)

        operations_count = d.pop("operationsCount", UNSET)

        work_count = d.pop("workCount", UNSET)

        kpi_unassigned_items_summary = cls(
            description=description,
            total_count=total_count,
            support_count=support_count,
            operations_count=operations_count,
            work_count=work_count,
        )

        kpi_unassigned_items_summary.additional_properties = d
        return kpi_unassigned_items_summary

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
