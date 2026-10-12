from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsMarginItem")


@_attrs_define
class AnalyticsMarginItem:
    """Margin for a single entity. Null wherever that entity holds a row with no rate.

    Attributes:
        name (str):
        revenue (float | None | str | Unset):
        costs (float | None | str | Unset):
        gross_margin (float | None | str | Unset):
        gross_margin_percent (float | None | str | Unset):
    """

    name: str
    revenue: float | None | str | Unset = UNSET
    costs: float | None | str | Unset = UNSET
    gross_margin: float | None | str | Unset = UNSET
    gross_margin_percent: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        revenue: float | None | str | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        costs: float | None | str | Unset
        if isinstance(self.costs, Unset):
            costs = UNSET
        else:
            costs = self.costs

        gross_margin: float | None | str | Unset
        if isinstance(self.gross_margin, Unset):
            gross_margin = UNSET
        else:
            gross_margin = self.gross_margin

        gross_margin_percent: float | None | str | Unset
        if isinstance(self.gross_margin_percent, Unset):
            gross_margin_percent = UNSET
        else:
            gross_margin_percent = self.gross_margin_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if costs is not UNSET:
            field_dict["costs"] = costs
        if gross_margin is not UNSET:
            field_dict["gross_margin"] = gross_margin
        if gross_margin_percent is not UNSET:
            field_dict["gross_margin_percent"] = gross_margin_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        def _parse_costs(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        costs = _parse_costs(d.pop("costs", UNSET))

        def _parse_gross_margin(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        gross_margin = _parse_gross_margin(d.pop("gross_margin", UNSET))

        def _parse_gross_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        gross_margin_percent = _parse_gross_margin_percent(
            d.pop("gross_margin_percent", UNSET)
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
