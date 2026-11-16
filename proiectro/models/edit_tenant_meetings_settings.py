from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenantMeetingsSettings")


@_attrs_define
class EditTenantMeetingsSettings:
    """The workspace's meeting pages (plans/PUBLIC_INBOUND.md D1). An omitted key keeps the stored
    value; an empty lead list or questions form means none. Minimum notice is in hours, the booking
    horizon in days.

        Attributes:
            enabled (bool | None | Unset):
            phone_required (bool | None | Unset):
            company_required (bool | None | Unset):
            lead_list (None | str | Unset):
            custom_form (None | str | Unset):
            min_notice_hours (int | None | Unset):
            horizon_days (int | None | Unset):
    """

    enabled: bool | None | Unset = UNSET
    phone_required: bool | None | Unset = UNSET
    company_required: bool | None | Unset = UNSET
    lead_list: None | str | Unset = UNSET
    custom_form: None | str | Unset = UNSET
    min_notice_hours: int | None | Unset = UNSET
    horizon_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        phone_required: bool | None | Unset
        if isinstance(self.phone_required, Unset):
            phone_required = UNSET
        else:
            phone_required = self.phone_required

        company_required: bool | None | Unset
        if isinstance(self.company_required, Unset):
            company_required = UNSET
        else:
            company_required = self.company_required

        lead_list: None | str | Unset
        if isinstance(self.lead_list, Unset):
            lead_list = UNSET
        else:
            lead_list = self.lead_list

        custom_form: None | str | Unset
        if isinstance(self.custom_form, Unset):
            custom_form = UNSET
        else:
            custom_form = self.custom_form

        min_notice_hours: int | None | Unset
        if isinstance(self.min_notice_hours, Unset):
            min_notice_hours = UNSET
        else:
            min_notice_hours = self.min_notice_hours

        horizon_days: int | None | Unset
        if isinstance(self.horizon_days, Unset):
            horizon_days = UNSET
        else:
            horizon_days = self.horizon_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if phone_required is not UNSET:
            field_dict["phone_required"] = phone_required
        if company_required is not UNSET:
            field_dict["company_required"] = company_required
        if lead_list is not UNSET:
            field_dict["lead_list"] = lead_list
        if custom_form is not UNSET:
            field_dict["custom_form"] = custom_form
        if min_notice_hours is not UNSET:
            field_dict["min_notice_hours"] = min_notice_hours
        if horizon_days is not UNSET:
            field_dict["horizon_days"] = horizon_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_phone_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        phone_required = _parse_phone_required(d.pop("phone_required", UNSET))

        def _parse_company_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        company_required = _parse_company_required(d.pop("company_required", UNSET))

        def _parse_lead_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_list = _parse_lead_list(d.pop("lead_list", UNSET))

        def _parse_custom_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_form = _parse_custom_form(d.pop("custom_form", UNSET))

        def _parse_min_notice_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_notice_hours = _parse_min_notice_hours(d.pop("min_notice_hours", UNSET))

        def _parse_horizon_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        horizon_days = _parse_horizon_days(d.pop("horizon_days", UNSET))

        edit_tenant_meetings_settings = cls(
            enabled=enabled,
            phone_required=phone_required,
            company_required=company_required,
            lead_list=lead_list,
            custom_form=custom_form,
            min_notice_hours=min_notice_hours,
            horizon_days=horizon_days,
        )

        edit_tenant_meetings_settings.additional_properties = d
        return edit_tenant_meetings_settings

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
