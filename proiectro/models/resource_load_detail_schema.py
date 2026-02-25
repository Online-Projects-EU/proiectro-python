from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.day_column_schema import DayColumnSchema
    from ..models.resource_load_detail_schema_resource_data_type_0 import (
        ResourceLoadDetailSchemaResourceDataType0,
    )


T = TypeVar("T", bound="ResourceLoadDetailSchema")


@_attrs_define
class ResourceLoadDetailSchema:
    """Detailed load data for an individual resource

    Attributes:
        resource_id (str):
        resource_name (str):
        period (str):
        start_date (str):
        end_date (str):
        week_dates (list[DayColumnSchema]):
        week_label (str):
        week_number (int):
        is_current (bool):
        is_past (bool):
        is_future (bool):
        resource_data (None | ResourceLoadDetailSchemaResourceDataType0):
        has_holidays (bool):
        max_bookings (int):
        booking_indices (list[int]):
        total_hours (float):
        total_available (float):
        utilization_percentage (float):
    """

    resource_id: str
    resource_name: str
    period: str
    start_date: str
    end_date: str
    week_dates: list[DayColumnSchema]
    week_label: str
    week_number: int
    is_current: bool
    is_past: bool
    is_future: bool
    resource_data: None | ResourceLoadDetailSchemaResourceDataType0
    has_holidays: bool
    max_bookings: int
    booking_indices: list[int]
    total_hours: float
    total_available: float
    utilization_percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_load_detail_schema_resource_data_type_0 import (
            ResourceLoadDetailSchemaResourceDataType0,
        )

        resource_id = self.resource_id

        resource_name = self.resource_name

        period = self.period

        start_date = self.start_date

        end_date = self.end_date

        week_dates = []
        for week_dates_item_data in self.week_dates:
            week_dates_item = week_dates_item_data.to_dict()
            week_dates.append(week_dates_item)

        week_label = self.week_label

        week_number = self.week_number

        is_current = self.is_current

        is_past = self.is_past

        is_future = self.is_future

        resource_data: dict[str, Any] | None
        if isinstance(self.resource_data, ResourceLoadDetailSchemaResourceDataType0):
            resource_data = self.resource_data.to_dict()
        else:
            resource_data = self.resource_data

        has_holidays = self.has_holidays

        max_bookings = self.max_bookings

        booking_indices = self.booking_indices

        total_hours = self.total_hours

        total_available = self.total_available

        utilization_percentage = self.utilization_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
                "resource_name": resource_name,
                "period": period,
                "start_date": start_date,
                "end_date": end_date,
                "week_dates": week_dates,
                "week_label": week_label,
                "week_number": week_number,
                "is_current": is_current,
                "is_past": is_past,
                "is_future": is_future,
                "resource_data": resource_data,
                "has_holidays": has_holidays,
                "max_bookings": max_bookings,
                "booking_indices": booking_indices,
                "total_hours": total_hours,
                "total_available": total_available,
                "utilization_percentage": utilization_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.day_column_schema import DayColumnSchema
        from ..models.resource_load_detail_schema_resource_data_type_0 import (
            ResourceLoadDetailSchemaResourceDataType0,
        )

        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        resource_name = d.pop("resource_name")

        period = d.pop("period")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        week_dates = []
        _week_dates = d.pop("week_dates")
        for week_dates_item_data in _week_dates:
            week_dates_item = DayColumnSchema.from_dict(week_dates_item_data)

            week_dates.append(week_dates_item)

        week_label = d.pop("week_label")

        week_number = d.pop("week_number")

        is_current = d.pop("is_current")

        is_past = d.pop("is_past")

        is_future = d.pop("is_future")

        def _parse_resource_data(
            data: object,
        ) -> None | ResourceLoadDetailSchemaResourceDataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resource_data_type_0 = (
                    ResourceLoadDetailSchemaResourceDataType0.from_dict(data)
                )

                return resource_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceLoadDetailSchemaResourceDataType0, data)

        resource_data = _parse_resource_data(d.pop("resource_data"))

        has_holidays = d.pop("has_holidays")

        max_bookings = d.pop("max_bookings")

        booking_indices = cast(list[int], d.pop("booking_indices"))

        total_hours = d.pop("total_hours")

        total_available = d.pop("total_available")

        utilization_percentage = d.pop("utilization_percentage")

        resource_load_detail_schema = cls(
            resource_id=resource_id,
            resource_name=resource_name,
            period=period,
            start_date=start_date,
            end_date=end_date,
            week_dates=week_dates,
            week_label=week_label,
            week_number=week_number,
            is_current=is_current,
            is_past=is_past,
            is_future=is_future,
            resource_data=resource_data,
            has_holidays=has_holidays,
            max_bookings=max_bookings,
            booking_indices=booking_indices,
            total_hours=total_hours,
            total_available=total_available,
            utilization_percentage=utilization_percentage,
        )

        resource_load_detail_schema.additional_properties = d
        return resource_load_detail_schema

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
