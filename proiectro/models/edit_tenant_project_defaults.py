from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenantProjectDefaults")


@_attrs_define
class EditTenantProjectDefaults:
    """Schema for updating default project settings.

    Attributes:
        project_enable_booking_management (bool | None | Unset):
        project_enable_resource_management (bool | None | Unset):
        project_enable_effort_management (bool | None | Unset):
        project_enable_financial_management (bool | None | Unset):
        project_enable_schedule_management (bool | None | Unset):
        project_enable_earned_value_management (bool | None | Unset):
        wbsconfiguration (None | str | Unset):
    """

    project_enable_booking_management: bool | None | Unset = UNSET
    project_enable_resource_management: bool | None | Unset = UNSET
    project_enable_effort_management: bool | None | Unset = UNSET
    project_enable_financial_management: bool | None | Unset = UNSET
    project_enable_schedule_management: bool | None | Unset = UNSET
    project_enable_earned_value_management: bool | None | Unset = UNSET
    wbsconfiguration: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
            project_enable_financial_management = (
                self.project_enable_financial_management
            )

        project_enable_schedule_management: bool | None | Unset
        if isinstance(self.project_enable_schedule_management, Unset):
            project_enable_schedule_management = UNSET
        else:
            project_enable_schedule_management = self.project_enable_schedule_management

        project_enable_earned_value_management: bool | None | Unset
        if isinstance(self.project_enable_earned_value_management, Unset):
            project_enable_earned_value_management = UNSET
        else:
            project_enable_earned_value_management = (
                self.project_enable_earned_value_management
            )

        wbsconfiguration: None | str | Unset
        if isinstance(self.wbsconfiguration, Unset):
            wbsconfiguration = UNSET
        else:
            wbsconfiguration = self.wbsconfiguration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_enable_booking_management is not UNSET:
            field_dict["project_enable_booking_management"] = (
                project_enable_booking_management
            )
        if project_enable_resource_management is not UNSET:
            field_dict["project_enable_resource_management"] = (
                project_enable_resource_management
            )
        if project_enable_effort_management is not UNSET:
            field_dict["project_enable_effort_management"] = (
                project_enable_effort_management
            )
        if project_enable_financial_management is not UNSET:
            field_dict["project_enable_financial_management"] = (
                project_enable_financial_management
            )
        if project_enable_schedule_management is not UNSET:
            field_dict["project_enable_schedule_management"] = (
                project_enable_schedule_management
            )
        if project_enable_earned_value_management is not UNSET:
            field_dict["project_enable_earned_value_management"] = (
                project_enable_earned_value_management
            )
        if wbsconfiguration is not UNSET:
            field_dict["wbsconfiguration"] = wbsconfiguration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_project_enable_booking_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_booking_management = _parse_project_enable_booking_management(
            d.pop("project_enable_booking_management", UNSET)
        )

        def _parse_project_enable_resource_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_resource_management = _parse_project_enable_resource_management(
            d.pop("project_enable_resource_management", UNSET)
        )

        def _parse_project_enable_effort_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_effort_management = _parse_project_enable_effort_management(
            d.pop("project_enable_effort_management", UNSET)
        )

        def _parse_project_enable_financial_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_financial_management = (
            _parse_project_enable_financial_management(
                d.pop("project_enable_financial_management", UNSET)
            )
        )

        def _parse_project_enable_schedule_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_schedule_management = _parse_project_enable_schedule_management(
            d.pop("project_enable_schedule_management", UNSET)
        )

        def _parse_project_enable_earned_value_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_earned_value_management = (
            _parse_project_enable_earned_value_management(
                d.pop("project_enable_earned_value_management", UNSET)
            )
        )

        def _parse_wbsconfiguration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbsconfiguration = _parse_wbsconfiguration(d.pop("wbsconfiguration", UNSET))

        edit_tenant_project_defaults = cls(
            project_enable_booking_management=project_enable_booking_management,
            project_enable_resource_management=project_enable_resource_management,
            project_enable_effort_management=project_enable_effort_management,
            project_enable_financial_management=project_enable_financial_management,
            project_enable_schedule_management=project_enable_schedule_management,
            project_enable_earned_value_management=project_enable_earned_value_management,
            wbsconfiguration=wbsconfiguration,
        )

        edit_tenant_project_defaults.additional_properties = d
        return edit_tenant_project_defaults

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
