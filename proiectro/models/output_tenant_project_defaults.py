from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputTenantProjectDefaults")


@_attrs_define
class OutputTenantProjectDefaults:
    """Output schema for tenant project default settings (GET endpoint).

    Attributes:
        enable_booking_management (bool | Unset):  Default: True.
        enable_resource_management (bool | Unset):  Default: True.
        enable_effort_management (bool | Unset):  Default: True.
        enable_financial_management (bool | Unset):  Default: True.
        enable_schedule_management (bool | Unset):  Default: True.
        enable_earned_value_management (bool | Unset):  Default: False.
        default_wbs_configuration_id (None | str | Unset):
        default_wbs_configuration_name (None | str | Unset):
    """

    enable_booking_management: bool | Unset = True
    enable_resource_management: bool | Unset = True
    enable_effort_management: bool | Unset = True
    enable_financial_management: bool | Unset = True
    enable_schedule_management: bool | Unset = True
    enable_earned_value_management: bool | Unset = False
    default_wbs_configuration_id: None | str | Unset = UNSET
    default_wbs_configuration_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_booking_management = self.enable_booking_management

        enable_resource_management = self.enable_resource_management

        enable_effort_management = self.enable_effort_management

        enable_financial_management = self.enable_financial_management

        enable_schedule_management = self.enable_schedule_management

        enable_earned_value_management = self.enable_earned_value_management

        default_wbs_configuration_id: None | str | Unset
        if isinstance(self.default_wbs_configuration_id, Unset):
            default_wbs_configuration_id = UNSET
        else:
            default_wbs_configuration_id = self.default_wbs_configuration_id

        default_wbs_configuration_name: None | str | Unset
        if isinstance(self.default_wbs_configuration_name, Unset):
            default_wbs_configuration_name = UNSET
        else:
            default_wbs_configuration_name = self.default_wbs_configuration_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_booking_management is not UNSET:
            field_dict["enable_booking_management"] = enable_booking_management
        if enable_resource_management is not UNSET:
            field_dict["enable_resource_management"] = enable_resource_management
        if enable_effort_management is not UNSET:
            field_dict["enable_effort_management"] = enable_effort_management
        if enable_financial_management is not UNSET:
            field_dict["enable_financial_management"] = enable_financial_management
        if enable_schedule_management is not UNSET:
            field_dict["enable_schedule_management"] = enable_schedule_management
        if enable_earned_value_management is not UNSET:
            field_dict["enable_earned_value_management"] = (
                enable_earned_value_management
            )
        if default_wbs_configuration_id is not UNSET:
            field_dict["default_wbs_configuration_id"] = default_wbs_configuration_id
        if default_wbs_configuration_name is not UNSET:
            field_dict["default_wbs_configuration_name"] = (
                default_wbs_configuration_name
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_booking_management = d.pop("enable_booking_management", UNSET)

        enable_resource_management = d.pop("enable_resource_management", UNSET)

        enable_effort_management = d.pop("enable_effort_management", UNSET)

        enable_financial_management = d.pop("enable_financial_management", UNSET)

        enable_schedule_management = d.pop("enable_schedule_management", UNSET)

        enable_earned_value_management = d.pop("enable_earned_value_management", UNSET)

        def _parse_default_wbs_configuration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_wbs_configuration_id = _parse_default_wbs_configuration_id(
            d.pop("default_wbs_configuration_id", UNSET)
        )

        def _parse_default_wbs_configuration_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_wbs_configuration_name = _parse_default_wbs_configuration_name(
            d.pop("default_wbs_configuration_name", UNSET)
        )

        output_tenant_project_defaults = cls(
            enable_booking_management=enable_booking_management,
            enable_resource_management=enable_resource_management,
            enable_effort_management=enable_effort_management,
            enable_financial_management=enable_financial_management,
            enable_schedule_management=enable_schedule_management,
            enable_earned_value_management=enable_earned_value_management,
            default_wbs_configuration_id=default_wbs_configuration_id,
            default_wbs_configuration_name=default_wbs_configuration_name,
        )

        output_tenant_project_defaults.additional_properties = d
        return output_tenant_project_defaults

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
