from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ProjectResourceActivityWeeklySchema")


@_attrs_define
class ProjectResourceActivityWeeklySchema:
    """Weekly aggregated resource usage data for project resource activity histogram

    Attributes:
        week_start (datetime.date):
        week_end (datetime.date):
        year_week (str):
        week_label (str):
        week_start_formatted (str):
        week_end_formatted (str):
        usage_count (int):
    """

    week_start: datetime.date
    week_end: datetime.date
    year_week: str
    week_label: str
    week_start_formatted: str
    week_end_formatted: str
    usage_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        week_start = self.week_start.isoformat()

        week_end = self.week_end.isoformat()

        year_week = self.year_week

        week_label = self.week_label

        week_start_formatted = self.week_start_formatted

        week_end_formatted = self.week_end_formatted

        usage_count = self.usage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "week_start": week_start,
                "week_end": week_end,
                "year_week": year_week,
                "week_label": week_label,
                "week_start_formatted": week_start_formatted,
                "week_end_formatted": week_end_formatted,
                "usage_count": usage_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        week_start = isoparse(d.pop("week_start")).date()

        week_end = isoparse(d.pop("week_end")).date()

        year_week = d.pop("year_week")

        week_label = d.pop("week_label")

        week_start_formatted = d.pop("week_start_formatted")

        week_end_formatted = d.pop("week_end_formatted")

        usage_count = d.pop("usage_count")

        project_resource_activity_weekly_schema = cls(
            week_start=week_start,
            week_end=week_end,
            year_week=year_week,
            week_label=week_label,
            week_start_formatted=week_start_formatted,
            week_end_formatted=week_end_formatted,
            usage_count=usage_count,
        )

        project_resource_activity_weekly_schema.additional_properties = d
        return project_resource_activity_weekly_schema

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
