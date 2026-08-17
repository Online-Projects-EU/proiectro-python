from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPILeadPipelineHealthSummary")



@_attrs_define
class KPILeadPipelineHealthSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            overdue_count (str | Unset):  Default: '0'.
            stale_count (str | Unset):  Default: '0'.
            unclaimed_count (str | Unset):  Default: '0'.
            untriaged_count (str | Unset):  Default: '0'.
            conversion_rate_30_d (str | Unset):  Default: '0'.
            max_rep_load (str | Unset):  Default: '0'.
            active_reps (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    overdue_count: str | Unset = '0'
    stale_count: str | Unset = '0'
    unclaimed_count: str | Unset = '0'
    untriaged_count: str | Unset = '0'
    conversion_rate_30_d: str | Unset = '0'
    max_rep_load: str | Unset = '0'
    active_reps: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        overdue_count = self.overdue_count

        stale_count = self.stale_count

        unclaimed_count = self.unclaimed_count

        untriaged_count = self.untriaged_count

        conversion_rate_30_d = self.conversion_rate_30_d

        max_rep_load = self.max_rep_load

        active_reps = self.active_reps


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if stale_count is not UNSET:
            field_dict["staleCount"] = stale_count
        if unclaimed_count is not UNSET:
            field_dict["unclaimedCount"] = unclaimed_count
        if untriaged_count is not UNSET:
            field_dict["untriagedCount"] = untriaged_count
        if conversion_rate_30_d is not UNSET:
            field_dict["conversionRate30d"] = conversion_rate_30_d
        if max_rep_load is not UNSET:
            field_dict["maxRepLoad"] = max_rep_load
        if active_reps is not UNSET:
            field_dict["activeReps"] = active_reps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        stale_count = d.pop("staleCount", UNSET)

        unclaimed_count = d.pop("unclaimedCount", UNSET)

        untriaged_count = d.pop("untriagedCount", UNSET)

        conversion_rate_30_d = d.pop("conversionRate30d", UNSET)

        max_rep_load = d.pop("maxRepLoad", UNSET)

        active_reps = d.pop("activeReps", UNSET)

        kpi_lead_pipeline_health_summary = cls(
            description=description,
            overdue_count=overdue_count,
            stale_count=stale_count,
            unclaimed_count=unclaimed_count,
            untriaged_count=untriaged_count,
            conversion_rate_30_d=conversion_rate_30_d,
            max_rep_load=max_rep_load,
            active_reps=active_reps,
        )


        kpi_lead_pipeline_health_summary.additional_properties = d
        return kpi_lead_pipeline_health_summary

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
