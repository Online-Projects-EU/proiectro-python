from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsMarginItem")


@_attrs_define
class AnalyticsMarginItem:
    """Margin for a single entity

    Attributes:
        name (str):
        revenue (float | str):
        costs (float | str):
        gross_margin (float | str):
        gross_margin_percent (float | str):
    """

    name: str
    revenue: float | str
    costs: float | str
    gross_margin: float | str
    gross_margin_percent: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        revenue: float | str
        revenue = self.revenue

        costs: float | str
        costs = self.costs

        gross_margin: float | str
        gross_margin = self.gross_margin

        gross_margin_percent: float | str
        gross_margin_percent = self.gross_margin_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "revenue": revenue,
                "costs": costs,
                "gross_margin": gross_margin,
                "gross_margin_percent": gross_margin_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_revenue(data: object) -> float | str:
            return cast(float | str, data)

        revenue = _parse_revenue(d.pop("revenue"))

        def _parse_costs(data: object) -> float | str:
            return cast(float | str, data)

        costs = _parse_costs(d.pop("costs"))

        def _parse_gross_margin(data: object) -> float | str:
            return cast(float | str, data)

        gross_margin = _parse_gross_margin(d.pop("gross_margin"))

        def _parse_gross_margin_percent(data: object) -> float | str:
            return cast(float | str, data)

        gross_margin_percent = _parse_gross_margin_percent(
            d.pop("gross_margin_percent")
        )

        analytics_margin_item = cls(
            name=name,
            revenue=revenue,
            costs=costs,
            gross_margin=gross_margin,
            gross_margin_percent=gross_margin_percent,
        )

        analytics_margin_item.additional_properties = d
        return analytics_margin_item

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
