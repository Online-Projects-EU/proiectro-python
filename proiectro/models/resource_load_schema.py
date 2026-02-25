from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.day_column_schema import DayColumnSchema
    from ..models.resource_load_schema_daily_totals import ResourceLoadSchemaDailyTotals
    from ..models.team_member_summary_schema import TeamMemberSummarySchema


T = TypeVar("T", bound="ResourceLoadSchema")


@_attrs_define
class ResourceLoadSchema:
    """Complete resource load data for a week - for all resources view

    Attributes:
        prev_week_param (str):
        next_week_param (str):
        prev_week_label (str):
        next_week_label (str):
        week_number (int):
        start_date (str):
        end_date (str):
        start_date_param (str):
        is_current_week (bool):
        is_past_week (bool):
        is_future_week (bool):
        columns (list[DayColumnSchema]):
        resources (list[TeamMemberSummarySchema]):
        daily_totals (ResourceLoadSchemaDailyTotals):
        resource_total_booked (float):
        resource_total_available (float):
        resource_total_display (str):
        resource_load_percentage (float):
    """

    prev_week_param: str
    next_week_param: str
    prev_week_label: str
    next_week_label: str
    week_number: int
    start_date: str
    end_date: str
    start_date_param: str
    is_current_week: bool
    is_past_week: bool
    is_future_week: bool
    columns: list[DayColumnSchema]
    resources: list[TeamMemberSummarySchema]
    daily_totals: ResourceLoadSchemaDailyTotals
    resource_total_booked: float
    resource_total_available: float
    resource_total_display: str
    resource_load_percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prev_week_param = self.prev_week_param

        next_week_param = self.next_week_param

        prev_week_label = self.prev_week_label

        next_week_label = self.next_week_label

        week_number = self.week_number

        start_date = self.start_date

        end_date = self.end_date

        start_date_param = self.start_date_param

        is_current_week = self.is_current_week

        is_past_week = self.is_past_week

        is_future_week = self.is_future_week

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        daily_totals = self.daily_totals.to_dict()

        resource_total_booked = self.resource_total_booked

        resource_total_available = self.resource_total_available

        resource_total_display = self.resource_total_display

        resource_load_percentage = self.resource_load_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prev_week_param": prev_week_param,
                "next_week_param": next_week_param,
                "prev_week_label": prev_week_label,
                "next_week_label": next_week_label,
                "week_number": week_number,
                "start_date": start_date,
                "end_date": end_date,
                "start_date_param": start_date_param,
                "is_current_week": is_current_week,
                "is_past_week": is_past_week,
                "is_future_week": is_future_week,
                "columns": columns,
                "resources": resources,
                "daily_totals": daily_totals,
                "resource_total_booked": resource_total_booked,
                "resource_total_available": resource_total_available,
                "resource_total_display": resource_total_display,
                "resource_load_percentage": resource_load_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.day_column_schema import DayColumnSchema
        from ..models.resource_load_schema_daily_totals import (
            ResourceLoadSchemaDailyTotals,
        )
        from ..models.team_member_summary_schema import TeamMemberSummarySchema

        d = dict(src_dict)
        prev_week_param = d.pop("prev_week_param")

        next_week_param = d.pop("next_week_param")

        prev_week_label = d.pop("prev_week_label")

        next_week_label = d.pop("next_week_label")

        week_number = d.pop("week_number")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        start_date_param = d.pop("start_date_param")

        is_current_week = d.pop("is_current_week")

        is_past_week = d.pop("is_past_week")

        is_future_week = d.pop("is_future_week")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = DayColumnSchema.from_dict(columns_item_data)

            columns.append(columns_item)

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = TeamMemberSummarySchema.from_dict(resources_item_data)

            resources.append(resources_item)

        daily_totals = ResourceLoadSchemaDailyTotals.from_dict(d.pop("daily_totals"))

        resource_total_booked = d.pop("resource_total_booked")

        resource_total_available = d.pop("resource_total_available")

        resource_total_display = d.pop("resource_total_display")

        resource_load_percentage = d.pop("resource_load_percentage")

        resource_load_schema = cls(
            prev_week_param=prev_week_param,
            next_week_param=next_week_param,
            prev_week_label=prev_week_label,
            next_week_label=next_week_label,
            week_number=week_number,
            start_date=start_date,
            end_date=end_date,
            start_date_param=start_date_param,
            is_current_week=is_current_week,
            is_past_week=is_past_week,
            is_future_week=is_future_week,
            columns=columns,
            resources=resources,
            daily_totals=daily_totals,
            resource_total_booked=resource_total_booked,
            resource_total_available=resource_total_available,
            resource_total_display=resource_total_display,
            resource_load_percentage=resource_load_percentage,
        )

        resource_load_schema.additional_properties = d
        return resource_load_schema

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
