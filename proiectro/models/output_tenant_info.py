from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.plan_info import PlanInfo





T = TypeVar("T", bound="OutputTenantInfo")



@_attrs_define
class OutputTenantInfo:
    """ Output schema for tenant preferences/info (GET endpoint).

        Attributes:
            name (str):
            timezone (str):
            default_currency (None | str | Unset):
            country (None | str | Unset):
            minimum_acceptable_margin (None | str | Unset):
            bridge_requests_allowed (bool | Unset):  Default: False.
            plan (None | PlanInfo | Unset):
     """

    name: str
    timezone: str
    default_currency: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    minimum_acceptable_margin: None | str | Unset = UNSET
    bridge_requests_allowed: bool | Unset = False
    plan: None | PlanInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.plan_info import PlanInfo
        name = self.name

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

        minimum_acceptable_margin: None | str | Unset
        if isinstance(self.minimum_acceptable_margin, Unset):
            minimum_acceptable_margin = UNSET
        else:
            minimum_acceptable_margin = self.minimum_acceptable_margin

        bridge_requests_allowed = self.bridge_requests_allowed

        plan: dict[str, Any] | None | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        elif isinstance(self.plan, PlanInfo):
            plan = self.plan.to_dict()
        else:
            plan = self.plan


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "timezone": timezone,
        })
        if default_currency is not UNSET:
            field_dict["default_currency"] = default_currency
        if country is not UNSET:
            field_dict["country"] = country
        if minimum_acceptable_margin is not UNSET:
            field_dict["minimum_acceptable_margin"] = minimum_acceptable_margin
        if bridge_requests_allowed is not UNSET:
            field_dict["bridge_requests_allowed"] = bridge_requests_allowed
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_info import PlanInfo
        d = dict(src_dict)
        name = d.pop("name")

        timezone = d.pop("timezone")

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


        def _parse_minimum_acceptable_margin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_acceptable_margin = _parse_minimum_acceptable_margin(d.pop("minimum_acceptable_margin", UNSET))


        bridge_requests_allowed = d.pop("bridge_requests_allowed", UNSET)

        def _parse_plan(data: object) -> None | PlanInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plan_type_0 = PlanInfo.from_dict(data)



                return plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlanInfo | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))


        output_tenant_info = cls(
            name=name,
            timezone=timezone,
            default_currency=default_currency,
            country=country,
            minimum_acceptable_margin=minimum_acceptable_margin,
            bridge_requests_allowed=bridge_requests_allowed,
            plan=plan,
        )


        output_tenant_info.additional_properties = d
        return output_tenant_info

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
