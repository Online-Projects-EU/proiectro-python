from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsCostCategoryItem")


@_attrs_define
class AnalyticsCostCategoryItem:
    """Costs by category. Null where that category holds an expense with no rate.

    Attributes:
        category (str):
        amount (float | None | str | Unset):
        percent_of_total (float | None | str | Unset):
    """

    category: str
    amount: float | None | str | Unset = UNSET
    percent_of_total: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        amount: float | None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        percent_of_total: float | None | str | Unset
        if isinstance(self.percent_of_total, Unset):
            percent_of_total = UNSET
        else:
            percent_of_total = self.percent_of_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if percent_of_total is not UNSET:
            field_dict["percent_of_total"] = percent_of_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        def _parse_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_percent_of_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        percent_of_total = _parse_percent_of_total(d.pop("percent_of_total", UNSET))

        analytics_cost_category_item = cls(
            category=category,
            amount=amount,
            percent_of_total=percent_of_total,
        )

        analytics_cost_category_item.additional_properties = d
        return analytics_cost_category_item

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
