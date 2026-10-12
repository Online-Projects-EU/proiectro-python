from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsCostMonthItem")


@_attrs_define
class AnalyticsCostMonthItem:
    """Costs for a single month. Null where that month holds an expense with no rate.

    Attributes:
        month (str):
        direct (float | None | str | Unset):
        overhead (float | None | str | Unset):
        total (float | None | str | Unset):
    """

    month: str
    direct: float | None | str | Unset = UNSET
    overhead: float | None | str | Unset = UNSET
    total: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        direct: float | None | str | Unset
        if isinstance(self.direct, Unset):
            direct = UNSET
        else:
            direct = self.direct

        overhead: float | None | str | Unset
        if isinstance(self.overhead, Unset):
            overhead = UNSET
        else:
            overhead = self.overhead

        total: float | None | str | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
            }
        )
        if direct is not UNSET:
            field_dict["direct"] = direct
        if overhead is not UNSET:
            field_dict["overhead"] = overhead
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        def _parse_direct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        direct = _parse_direct(d.pop("direct", UNSET))

        def _parse_overhead(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        overhead = _parse_overhead(d.pop("overhead", UNSET))

        def _parse_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        analytics_cost_month_item = cls(
            month=month,
            direct=direct,
            overhead=overhead,
            total=total,
        )

        analytics_cost_month_item.additional_properties = d
        return analytics_cost_month_item

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
