from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KPIProcessBottlenecksSummary")


@_attrs_define
class KPIProcessBottlenecksSummary:
    """
    Attributes:
        description (str | Unset):  Default: ''.
        bottleneck_count (str | Unset):  Default: '0'.
        total_items_blocked (str | Unset):  Default: '0'.
        worst_stage (str | Unset):  Default: ''.
        worst_stage_count (str | Unset):  Default: '0'.
    """

    description: str | Unset = ""
    bottleneck_count: str | Unset = "0"
    total_items_blocked: str | Unset = "0"
    worst_stage: str | Unset = ""
    worst_stage_count: str | Unset = "0"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        bottleneck_count = self.bottleneck_count

        total_items_blocked = self.total_items_blocked

        worst_stage = self.worst_stage

        worst_stage_count = self.worst_stage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if bottleneck_count is not UNSET:
            field_dict["bottleneckCount"] = bottleneck_count
        if total_items_blocked is not UNSET:
            field_dict["totalItemsBlocked"] = total_items_blocked
        if worst_stage is not UNSET:
            field_dict["worstStage"] = worst_stage
        if worst_stage_count is not UNSET:
            field_dict["worstStageCount"] = worst_stage_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        bottleneck_count = d.pop("bottleneckCount", UNSET)

        total_items_blocked = d.pop("totalItemsBlocked", UNSET)

        worst_stage = d.pop("worstStage", UNSET)

        worst_stage_count = d.pop("worstStageCount", UNSET)

        kpi_process_bottlenecks_summary = cls(
            description=description,
            bottleneck_count=bottleneck_count,
            total_items_blocked=total_items_blocked,
            worst_stage=worst_stage,
            worst_stage_count=worst_stage_count,
        )

        kpi_process_bottlenecks_summary.additional_properties = d
        return kpi_process_bottlenecks_summary

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
