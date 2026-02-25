from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectResourceBooking")


@_attrs_define
class ProjectResourceBooking:
    """Individual resource booking for a project

    Attributes:
        id (str):
        resource_name (str):
        start_date (str):
        hours_per_day (float):
        name (str):
        is_active (bool):
        resource_type (None | str | Unset):
        end_date (None | str | Unset):
    """

    id: str
    resource_name: str
    start_date: str
    hours_per_day: float
    name: str
    is_active: bool
    resource_type: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_name = self.resource_name

        start_date = self.start_date

        hours_per_day = self.hours_per_day

        name = self.name

        is_active = self.is_active

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resource_name": resource_name,
                "start_date": start_date,
                "hours_per_day": hours_per_day,
                "name": name,
                "is_active": is_active,
            }
        )
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        resource_name = d.pop("resource_name")

        start_date = d.pop("start_date")

        hours_per_day = d.pop("hours_per_day")

        name = d.pop("name")

        is_active = d.pop("is_active")

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resource_type", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        project_resource_booking = cls(
            id=id,
            resource_name=resource_name,
            start_date=start_date,
            hours_per_day=hours_per_day,
            name=name,
            is_active=is_active,
            resource_type=resource_type,
            end_date=end_date,
        )

        project_resource_booking.additional_properties = d
        return project_resource_booking

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
