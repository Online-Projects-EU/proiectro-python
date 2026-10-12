from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.project_resource_activity_weekly_schema import (
        ProjectResourceActivityWeeklySchema,
    )


T = TypeVar("T", bound="ProjectResourceActivityHistogramSchema")


@_attrs_define
class ProjectResourceActivityHistogramSchema:
    """Project resource activity histogram data for visualization

    Attributes:
        resource_id (str):
        resource_name (str):
        project_id (str):
        project_name (str):
        weeks (list[ProjectResourceActivityWeeklySchema]):
        start_date (datetime.date):
        end_date (datetime.date):
        max_usage (int):
        total_usage (int):
    """

    resource_id: str
    resource_name: str
    project_id: str
    project_name: str
    weeks: list[ProjectResourceActivityWeeklySchema]
    start_date: datetime.date
    end_date: datetime.date
    max_usage: int
    total_usage: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_name = self.resource_name

        project_id = self.project_id

        project_name = self.project_name

        weeks = []
        for weeks_item_data in self.weeks:
            weeks_item = weeks_item_data.to_dict()
            weeks.append(weeks_item)

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        max_usage = self.max_usage

        total_usage = self.total_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
                "resource_name": resource_name,
                "project_id": project_id,
                "project_name": project_name,
                "weeks": weeks,
                "start_date": start_date,
                "end_date": end_date,
                "max_usage": max_usage,
                "total_usage": total_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_resource_activity_weekly_schema import (
            ProjectResourceActivityWeeklySchema,
        )

        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        resource_name = d.pop("resource_name")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        weeks = []
        _weeks = d.pop("weeks")
        for weeks_item_data in _weeks:
            weeks_item = ProjectResourceActivityWeeklySchema.from_dict(weeks_item_data)

            weeks.append(weeks_item)

        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        max_usage = d.pop("max_usage")

        total_usage = d.pop("total_usage")

        project_resource_activity_histogram_schema = cls(
            resource_id=resource_id,
            resource_name=resource_name,
            project_id=project_id,
            project_name=project_name,
            weeks=weeks,
            start_date=start_date,
            end_date=end_date,
            max_usage=max_usage,
            total_usage=total_usage,
        )

        project_resource_activity_histogram_schema.additional_properties = d
        return project_resource_activity_histogram_schema

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
