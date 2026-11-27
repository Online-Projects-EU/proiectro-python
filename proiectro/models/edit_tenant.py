from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_tenant_lead_visibility_type_0 import EditTenantLeadVisibilityType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenant")


@_attrs_define
class EditTenant:
    """
    Attributes:
        name (None | str | Unset):
        timezone (None | str | Unset):
        default_currency (None | str | Unset):
        country (None | str | Unset):
        minimum_acceptable_margin (float | None | str | Unset):
        bridge_requests_allowed (bool | None | Unset):
        lead_visibility (EditTenantLeadVisibilityType0 | None | Unset):
        geo_capture_max_accuracy_m (int | None | Unset):
        geofence_enabled (bool | None | Unset):
        geofence_radius_m (int | None | Unset):
        time_off_requires_approval (bool | None | Unset):
        llm_may_change_data (bool | None | Unset):
        intake_owner (None | str | Unset):
        intake_role (None | str | Unset):
        intake_lead_list (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    default_currency: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    minimum_acceptable_margin: float | None | str | Unset = UNSET
    bridge_requests_allowed: bool | None | Unset = UNSET
    lead_visibility: EditTenantLeadVisibilityType0 | None | Unset = UNSET
    geo_capture_max_accuracy_m: int | None | Unset = UNSET
    geofence_enabled: bool | None | Unset = UNSET
    geofence_radius_m: int | None | Unset = UNSET
    time_off_requires_approval: bool | None | Unset = UNSET
    llm_may_change_data: bool | None | Unset = UNSET
    intake_owner: None | str | Unset = UNSET
    intake_role: None | str | Unset = UNSET
    intake_lead_list: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        default_currency: None | str | Unset
        if isinstance(self.default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = self.default_currency

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        minimum_acceptable_margin: float | None | str | Unset
        if isinstance(self.minimum_acceptable_margin, Unset):
            minimum_acceptable_margin = UNSET
        else:
            minimum_acceptable_margin = self.minimum_acceptable_margin

        bridge_requests_allowed: bool | None | Unset
        if isinstance(self.bridge_requests_allowed, Unset):
            bridge_requests_allowed = UNSET
        else:
            bridge_requests_allowed = self.bridge_requests_allowed

        lead_visibility: None | str | Unset
        if isinstance(self.lead_visibility, Unset):
            lead_visibility = UNSET
        elif isinstance(self.lead_visibility, EditTenantLeadVisibilityType0):
            lead_visibility = self.lead_visibility.value
        else:
            lead_visibility = self.lead_visibility

        geo_capture_max_accuracy_m: int | None | Unset
        if isinstance(self.geo_capture_max_accuracy_m, Unset):
            geo_capture_max_accuracy_m = UNSET
        else:
            geo_capture_max_accuracy_m = self.geo_capture_max_accuracy_m

        geofence_enabled: bool | None | Unset
        if isinstance(self.geofence_enabled, Unset):
            geofence_enabled = UNSET
        else:
            geofence_enabled = self.geofence_enabled

        geofence_radius_m: int | None | Unset
        if isinstance(self.geofence_radius_m, Unset):
            geofence_radius_m = UNSET
        else:
            geofence_radius_m = self.geofence_radius_m

        time_off_requires_approval: bool | None | Unset
        if isinstance(self.time_off_requires_approval, Unset):
            time_off_requires_approval = UNSET
        else:
            time_off_requires_approval = self.time_off_requires_approval

        llm_may_change_data: bool | None | Unset
        if isinstance(self.llm_may_change_data, Unset):
            llm_may_change_data = UNSET
        else:
            llm_may_change_data = self.llm_may_change_data

        intake_owner: None | str | Unset
        if isinstance(self.intake_owner, Unset):
            intake_owner = UNSET
        else:
            intake_owner = self.intake_owner

        intake_role: None | str | Unset
        if isinstance(self.intake_role, Unset):
            intake_role = UNSET
        else:
            intake_role = self.intake_role

        intake_lead_list: None | str | Unset
        if isinstance(self.intake_lead_list, Unset):
            intake_lead_list = UNSET
        else:
            intake_lead_list = self.intake_lead_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if default_currency is not UNSET:
            field_dict["default_currency"] = default_currency
        if country is not UNSET:
            field_dict["country"] = country
        if minimum_acceptable_margin is not UNSET:
            field_dict["minimum_acceptable_margin"] = minimum_acceptable_margin
        if bridge_requests_allowed is not UNSET:
            field_dict["bridge_requests_allowed"] = bridge_requests_allowed
        if lead_visibility is not UNSET:
            field_dict["lead_visibility"] = lead_visibility
        if geo_capture_max_accuracy_m is not UNSET:
            field_dict["geo_capture_max_accuracy_m"] = geo_capture_max_accuracy_m
        if geofence_enabled is not UNSET:
            field_dict["geofence_enabled"] = geofence_enabled
        if geofence_radius_m is not UNSET:
            field_dict["geofence_radius_m"] = geofence_radius_m
        if time_off_requires_approval is not UNSET:
            field_dict["time_off_requires_approval"] = time_off_requires_approval
        if llm_may_change_data is not UNSET:
            field_dict["llm_may_change_data"] = llm_may_change_data
        if intake_owner is not UNSET:
            field_dict["intake_owner"] = intake_owner
        if intake_role is not UNSET:
            field_dict["intake_role"] = intake_role
        if intake_lead_list is not UNSET:
            field_dict["intake_lead_list"] = intake_lead_list

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

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_default_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_currency = _parse_default_currency(d.pop("default_currency", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_minimum_acceptable_margin(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        minimum_acceptable_margin = _parse_minimum_acceptable_margin(
            d.pop("minimum_acceptable_margin", UNSET)
        )

        def _parse_bridge_requests_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        bridge_requests_allowed = _parse_bridge_requests_allowed(
            d.pop("bridge_requests_allowed", UNSET)
        )

        def _parse_lead_visibility(
            data: object,
        ) -> EditTenantLeadVisibilityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lead_visibility_type_0 = EditTenantLeadVisibilityType0(data)

                return lead_visibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditTenantLeadVisibilityType0 | None | Unset, data)

        lead_visibility = _parse_lead_visibility(d.pop("lead_visibility", UNSET))

        def _parse_geo_capture_max_accuracy_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        geo_capture_max_accuracy_m = _parse_geo_capture_max_accuracy_m(
            d.pop("geo_capture_max_accuracy_m", UNSET)
        )

        def _parse_geofence_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        geofence_enabled = _parse_geofence_enabled(d.pop("geofence_enabled", UNSET))

        def _parse_geofence_radius_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        geofence_radius_m = _parse_geofence_radius_m(d.pop("geofence_radius_m", UNSET))

        def _parse_time_off_requires_approval(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        time_off_requires_approval = _parse_time_off_requires_approval(
            d.pop("time_off_requires_approval", UNSET)
        )

        def _parse_llm_may_change_data(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        llm_may_change_data = _parse_llm_may_change_data(
            d.pop("llm_may_change_data", UNSET)
        )

        def _parse_intake_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intake_owner = _parse_intake_owner(d.pop("intake_owner", UNSET))

        def _parse_intake_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intake_role = _parse_intake_role(d.pop("intake_role", UNSET))

        def _parse_intake_lead_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intake_lead_list = _parse_intake_lead_list(d.pop("intake_lead_list", UNSET))

        edit_tenant = cls(
            name=name,
            timezone=timezone,
            default_currency=default_currency,
            country=country,
            minimum_acceptable_margin=minimum_acceptable_margin,
            bridge_requests_allowed=bridge_requests_allowed,
            lead_visibility=lead_visibility,
            geo_capture_max_accuracy_m=geo_capture_max_accuracy_m,
            geofence_enabled=geofence_enabled,
            geofence_radius_m=geofence_radius_m,
            time_off_requires_approval=time_off_requires_approval,
            llm_may_change_data=llm_may_change_data,
            intake_owner=intake_owner,
            intake_role=intake_role,
            intake_lead_list=intake_lead_list,
        )

        edit_tenant.additional_properties = d
        return edit_tenant

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
