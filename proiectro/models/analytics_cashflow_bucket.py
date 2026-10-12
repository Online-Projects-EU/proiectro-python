from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsCashflowBucket")


@_attrs_define
class AnalyticsCashflowBucket:
    """Cash flow for a single time bucket (quarter, month, or week)

    Attributes:
        label (str):
        sublabel (str):
        income_projected (float | None | str | Unset):
        income_realized (float | None | str | Unset):
        payments_projected (float | None | str | Unset):
        payments_realized (float | None | str | Unset):
        net_projected (float | None | str | Unset):
        net_realized (float | None | str | Unset):
    """

    label: str
    sublabel: str
    income_projected: float | None | str | Unset = UNSET
    income_realized: float | None | str | Unset = UNSET
    payments_projected: float | None | str | Unset = UNSET
    payments_realized: float | None | str | Unset = UNSET
    net_projected: float | None | str | Unset = UNSET
    net_realized: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        sublabel = self.sublabel

        income_projected: float | None | str | Unset
        if isinstance(self.income_projected, Unset):
            income_projected = UNSET
        else:
            income_projected = self.income_projected

        income_realized: float | None | str | Unset
        if isinstance(self.income_realized, Unset):
            income_realized = UNSET
        else:
            income_realized = self.income_realized

        payments_projected: float | None | str | Unset
        if isinstance(self.payments_projected, Unset):
            payments_projected = UNSET
        else:
            payments_projected = self.payments_projected

        payments_realized: float | None | str | Unset
        if isinstance(self.payments_realized, Unset):
            payments_realized = UNSET
        else:
            payments_realized = self.payments_realized

        net_projected: float | None | str | Unset
        if isinstance(self.net_projected, Unset):
            net_projected = UNSET
        else:
            net_projected = self.net_projected

        net_realized: float | None | str | Unset
        if isinstance(self.net_realized, Unset):
            net_realized = UNSET
        else:
            net_realized = self.net_realized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "sublabel": sublabel,
            }
        )
        if income_projected is not UNSET:
            field_dict["income_projected"] = income_projected
        if income_realized is not UNSET:
            field_dict["income_realized"] = income_realized
        if payments_projected is not UNSET:
            field_dict["payments_projected"] = payments_projected
        if payments_realized is not UNSET:
            field_dict["payments_realized"] = payments_realized
        if net_projected is not UNSET:
            field_dict["net_projected"] = net_projected
        if net_realized is not UNSET:
            field_dict["net_realized"] = net_realized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        sublabel = d.pop("sublabel")

        def _parse_income_projected(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        income_projected = _parse_income_projected(d.pop("income_projected", UNSET))

        def _parse_income_realized(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        income_realized = _parse_income_realized(d.pop("income_realized", UNSET))

        def _parse_payments_projected(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        payments_projected = _parse_payments_projected(
            d.pop("payments_projected", UNSET)
        )

        def _parse_payments_realized(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        payments_realized = _parse_payments_realized(d.pop("payments_realized", UNSET))

        def _parse_net_projected(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        net_projected = _parse_net_projected(d.pop("net_projected", UNSET))

        def _parse_net_realized(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        net_realized = _parse_net_realized(d.pop("net_realized", UNSET))

        analytics_cashflow_bucket = cls(
            label=label,
            sublabel=sublabel,
            income_projected=income_projected,
            income_realized=income_realized,
            payments_projected=payments_projected,
            payments_realized=payments_realized,
            net_projected=net_projected,
            net_realized=net_realized,
        )

        analytics_cashflow_bucket.additional_properties = d
        return analytics_cashflow_bucket

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
