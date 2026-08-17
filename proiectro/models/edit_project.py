from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="EditProject")



@_attrs_define
class EditProject:
    """ 
        Attributes:
            name (str):
            description (str):
            manager (str):
            internal_code (None | str | Unset):
            project_start_date (None | str | Unset):
            project_end_date (None | str | Unset):
            project_enable_booking_management (bool | None | Unset):
            project_enable_resource_management (bool | None | Unset):
            project_enable_effort_management (bool | None | Unset):
            project_enable_financial_management (bool | None | Unset):
            project_enable_schedule_management (bool | None | Unset):
            project_enable_earned_value_management (bool | None | Unset):
     """

    name: str
    description: str
    manager: str
    internal_code: None | str | Unset = UNSET
    project_start_date: None | str | Unset = UNSET
    project_end_date: None | str | Unset = UNSET
    project_enable_booking_management: bool | None | Unset = UNSET
    project_enable_resource_management: bool | None | Unset = UNSET
    project_enable_effort_management: bool | None | Unset = UNSET
    project_enable_financial_management: bool | None | Unset = UNSET
    project_enable_schedule_management: bool | None | Unset = UNSET
    project_enable_earned_value_management: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        manager = self.manager

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        project_start_date: None | str | Unset
        if isinstance(self.project_start_date, Unset):
            project_start_date = UNSET
        else:
            project_start_date = self.project_start_date

        project_end_date: None | str | Unset
        if isinstance(self.project_end_date, Unset):
            project_end_date = UNSET
        else:
            project_end_date = self.project_end_date

        project_enable_booking_management: bool | None | Unset
        if isinstance(self.project_enable_booking_management, Unset):
            project_enable_booking_management = UNSET
        else:
            project_enable_booking_management = self.project_enable_booking_management

        project_enable_resource_management: bool | None | Unset
        if isinstance(self.project_enable_resource_management, Unset):
            project_enable_resource_management = UNSET
        else:
            project_enable_resource_management = self.project_enable_resource_management

        project_enable_effort_management: bool | None | Unset
        if isinstance(self.project_enable_effort_management, Unset):
            project_enable_effort_management = UNSET
        else:
            project_enable_effort_management = self.project_enable_effort_management

        project_enable_financial_management: bool | None | Unset
        if isinstance(self.project_enable_financial_management, Unset):
            project_enable_financial_management = UNSET
        else:
            project_enable_financial_management = self.project_enable_financial_management

        project_enable_schedule_management: bool | None | Unset
        if isinstance(self.project_enable_schedule_management, Unset):
            project_enable_schedule_management = UNSET
        else:
            project_enable_schedule_management = self.project_enable_schedule_management

        project_enable_earned_value_management: bool | None | Unset
        if isinstance(self.project_enable_earned_value_management, Unset):
            project_enable_earned_value_management = UNSET
        else:
            project_enable_earned_value_management = self.project_enable_earned_value_management


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "description": description,
            "manager": manager,
        })
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if project_start_date is not UNSET:
            field_dict["project_start_date"] = project_start_date
        if project_end_date is not UNSET:
            field_dict["project_end_date"] = project_end_date
        if project_enable_booking_management is not UNSET:
            field_dict["project_enable_booking_management"] = project_enable_booking_management
        if project_enable_resource_management is not UNSET:
            field_dict["project_enable_resource_management"] = project_enable_resource_management
        if project_enable_effort_management is not UNSET:
            field_dict["project_enable_effort_management"] = project_enable_effort_management
        if project_enable_financial_management is not UNSET:
            field_dict["project_enable_financial_management"] = project_enable_financial_management
        if project_enable_schedule_management is not UNSET:
            field_dict["project_enable_schedule_management"] = project_enable_schedule_management
        if project_enable_earned_value_management is not UNSET:
            field_dict["project_enable_earned_value_management"] = project_enable_earned_value_management

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        manager = d.pop("manager")

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))


        def _parse_project_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_start_date = _parse_project_start_date(d.pop("project_start_date", UNSET))


        def _parse_project_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_end_date = _parse_project_end_date(d.pop("project_end_date", UNSET))


        def _parse_project_enable_booking_management(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_booking_management = _parse_project_enable_booking_management(d.pop("project_enable_booking_management", UNSET))


        def _parse_project_enable_resource_management(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_resource_management = _parse_project_enable_resource_management(d.pop("project_enable_resource_management", UNSET))


        def _parse_project_enable_effort_management(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_effort_management = _parse_project_enable_effort_management(d.pop("project_enable_effort_management", UNSET))


        def _parse_project_enable_financial_management(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_financial_management = _parse_project_enable_financial_management(d.pop("project_enable_financial_management", UNSET))


        def _parse_project_enable_schedule_management(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_schedule_management = _parse_project_enable_schedule_management(d.pop("project_enable_schedule_management", UNSET))


        def _parse_project_enable_earned_value_management(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_earned_value_management = _parse_project_enable_earned_value_management(d.pop("project_enable_earned_value_management", UNSET))


        edit_project = cls(
            name=name,
            description=description,
            manager=manager,
            internal_code=internal_code,
            project_start_date=project_start_date,
            project_end_date=project_end_date,
            project_enable_booking_management=project_enable_booking_management,
            project_enable_resource_management=project_enable_resource_management,
            project_enable_effort_management=project_enable_effort_management,
            project_enable_financial_management=project_enable_financial_management,
            project_enable_schedule_management=project_enable_schedule_management,
            project_enable_earned_value_management=project_enable_earned_value_management,
        )


        edit_project.additional_properties = d
        return edit_project

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
