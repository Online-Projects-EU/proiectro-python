from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="EditTimer")



@_attrs_define
class EditTimer:
    """ 
        Attributes:
            name (None | str | Unset):
            description (None | str | Unset):
            is_enabled (bool | Unset):  Default: False.
            schedule_type (None | str | Unset):
            schedule_hour (int | None | Unset):
            schedule_day_of_week (int | None | Unset):
            schedule_day_of_month (int | None | Unset):
     """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_enabled: bool | Unset = False
    schedule_type: None | str | Unset = UNSET
    schedule_hour: int | None | Unset = UNSET
    schedule_day_of_week: int | None | Unset = UNSET
    schedule_day_of_month: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_enabled = self.is_enabled

        schedule_type: None | str | Unset
        if isinstance(self.schedule_type, Unset):
            schedule_type = UNSET
        else:
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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if schedule_type is not UNSET:
            field_dict["schedule_type"] = schedule_type
        if schedule_hour is not UNSET:
            field_dict["schedule_hour"] = schedule_hour
        if schedule_day_of_week is not UNSET:
            field_dict["schedule_day_of_week"] = schedule_day_of_week
        if schedule_day_of_month is not UNSET:
            field_dict["schedule_day_of_month"] = schedule_day_of_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        is_enabled = d.pop("is_enabled", UNSET)

        def _parse_schedule_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schedule_type = _parse_schedule_type(d.pop("schedule_type", UNSET))


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

        schedule_day_of_week = _parse_schedule_day_of_week(d.pop("schedule_day_of_week", UNSET))


        def _parse_schedule_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule_day_of_month = _parse_schedule_day_of_month(d.pop("schedule_day_of_month", UNSET))


        edit_timer = cls(
            name=name,
            description=description,
            is_enabled=is_enabled,
            schedule_type=schedule_type,
            schedule_hour=schedule_hour,
            schedule_day_of_week=schedule_day_of_week,
            schedule_day_of_month=schedule_day_of_month,
        )


        edit_timer.additional_properties = d
        return edit_timer

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
