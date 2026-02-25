from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsCashflowBucket")


@_attrs_define
class AnalyticsCashflowBucket:
    """Cash flow for a single time bucket (quarter, month, or week)

    Attributes:
        label (str):
        sublabel (str):
        income_projected (float | str):
        income_realized (float | str):
        payments_projected (float | str):
        payments_realized (float | str):
        net_projected (float | str):
        net_realized (float | str):
    """

    label: str
    sublabel: str
    income_projected: float | str
    income_realized: float | str
    payments_projected: float | str
    payments_realized: float | str
    net_projected: float | str
    net_realized: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        sublabel = self.sublabel

        income_projected: float | str
        income_projected = self.income_projected

        income_realized: float | str
        income_realized = self.income_realized

        payments_projected: float | str
        payments_projected = self.payments_projected

        payments_realized: float | str
        payments_realized = self.payments_realized

        net_projected: float | str
        net_projected = self.net_projected

        net_realized: float | str
        net_realized = self.net_realized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "sublabel": sublabel,
                "income_projected": income_projected,
                "income_realized": income_realized,
                "payments_projected": payments_projected,
                "payments_realized": payments_realized,
                "net_projected": net_projected,
                "net_realized": net_realized,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        sublabel = d.pop("sublabel")

        def _parse_income_projected(data: object) -> float | str:
            return cast(float | str, data)

        income_projected = _parse_income_projected(d.pop("income_projected"))

        def _parse_income_realized(data: object) -> float | str:
            return cast(float | str, data)

        income_realized = _parse_income_realized(d.pop("income_realized"))

        def _parse_payments_projected(data: object) -> float | str:
            return cast(float | str, data)

        payments_projected = _parse_payments_projected(d.pop("payments_projected"))

        def _parse_payments_realized(data: object) -> float | str:
            return cast(float | str, data)

        payments_realized = _parse_payments_realized(d.pop("payments_realized"))

        def _parse_net_projected(data: object) -> float | str:
            return cast(float | str, data)

        net_projected = _parse_net_projected(d.pop("net_projected"))

        def _parse_net_realized(data: object) -> float | str:
            return cast(float | str, data)

        net_realized = _parse_net_realized(d.pop("net_realized"))

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
