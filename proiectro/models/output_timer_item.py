from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputTimerItem")


@_attrs_define
class OutputTimerItem:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        is_enabled (bool):
        schedule_type (str):
        schedule_hour (int | None | Unset):
        schedule_day_of_week (int | None | Unset):
        schedule_day_of_month (int | None | Unset):
        last_executed_at (datetime.datetime | None | Unset):
        next_execution_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    description: str
    is_enabled: bool
    schedule_type: str
    schedule_hour: int | None | Unset = UNSET
    schedule_day_of_week: int | None | Unset = UNSET
    schedule_day_of_month: int | None | Unset = UNSET
    last_executed_at: datetime.datetime | None | Unset = UNSET
    next_execution_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_enabled = self.is_enabled

        schedule_type = self.schedule_type

        schedule_hour: int | None | Unset
        if isinstance(self.schedule_hour, Unset):
            schedule_hour = UNSET
        else:
            schedule_hour = self.schedule_hour

        schedule_day_of_week: int | None | Unset
        if isinstance(self.schedule_day_of_week, Unset):
            schedule_day_of_week = UNSET
        else:
            schedule_day_of_week = self.schedule_day_of_week

        schedule_day_of_month: int | None | Unset
        if isinstance(self.schedule_day_of_month, Unset):
            schedule_day_of_month = UNSET
        else:
            schedule_day_of_month = self.schedule_day_of_month

        last_executed_at: None | str | Unset
        if isinstance(self.last_executed_at, Unset):
            last_executed_at = UNSET
        elif isinstance(self.last_executed_at, datetime.datetime):
            last_executed_at = self.last_executed_at.isoformat()
        else:
            last_executed_at = self.last_executed_at

        next_execution_at: None | str | Unset
        if isinstance(self.next_execution_at, Unset):
            next_execution_at = UNSET
        elif isinstance(self.next_execution_at, datetime.datetime):
            next_execution_at = self.next_execution_at.isoformat()
        else:
            next_execution_at = self.next_execution_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_enabled": is_enabled,
                "schedule_type": schedule_type,
            }
        )
        if schedule_hour is not UNSET:
            field_dict["schedule_hour"] = schedule_hour
        if schedule_day_of_week is not UNSET:
            field_dict["schedule_day_of_week"] = schedule_day_of_week
        if schedule_day_of_month is not UNSET:
            field_dict["schedule_day_of_month"] = schedule_day_of_month
        if last_executed_at is not UNSET:
            field_dict["last_executed_at"] = last_executed_at
        if next_execution_at is not UNSET:
            field_dict["next_execution_at"] = next_execution_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_enabled = d.pop("is_enabled")

        schedule_type = d.pop("schedule_type")

        def _parse_schedule_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule_hour = _parse_schedule_hour(d.pop("schedule_hour", UNSET))

        def _parse_schedule_day_of_week(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule_day_of_week = _parse_schedule_day_of_week(
            d.pop("schedule_day_of_week", UNSET)
        )

        def _parse_schedule_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule_day_of_month = _parse_schedule_day_of_month(
            d.pop("schedule_day_of_month", UNSET)
        )

        def _parse_last_executed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_executed_at_type_0 = isoparse(data)

                return last_executed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_executed_at = _parse_last_executed_at(d.pop("last_executed_at", UNSET))

        def _parse_next_execution_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_execution_at_type_0 = isoparse(data)

                return next_execution_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_execution_at = _parse_next_execution_at(d.pop("next_execution_at", UNSET))

        output_timer_item = cls(
            id=id,
            name=name,
            description=description,
            is_enabled=is_enabled,
            schedule_type=schedule_type,
            schedule_hour=schedule_hour,
            schedule_day_of_week=schedule_day_of_week,
            schedule_day_of_month=schedule_day_of_month,
            last_executed_at=last_executed_at,
            next_execution_at=next_execution_at,
        )

        output_timer_item.additional_properties = d
        return output_timer_item

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
