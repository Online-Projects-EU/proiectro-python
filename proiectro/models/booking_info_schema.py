from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingInfoSchema")


@_attrs_define
class BookingInfoSchema:
    """Individual booking information

    Attributes:
        name (str):
        project_name (str):
        hours (float):
        only_working_days (bool):
        project_id (None | str | Unset):
    """

    name: str
    project_name: str
    hours: float
    only_working_days: bool
    project_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_name = self.project_name

        hours = self.hours

        only_working_days = self.only_working_days

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project_name": project_name,
                "hours": hours,
                "only_working_days": only_working_days,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        project_name = d.pop("project_name")

        hours = d.pop("hours")

        only_working_days = d.pop("only_working_days")

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        booking_info_schema = cls(
            name=name,
            project_name=project_name,
            hours=hours,
            only_working_days=only_working_days,
            project_id=project_id,
        )

        booking_info_schema.additional_properties = d
        return booking_info_schema

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
