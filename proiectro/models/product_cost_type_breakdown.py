from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductCostTypeBreakdown")


@_attrs_define
class ProductCostTypeBreakdown:
    """Cost type breakdown for a single cost type in a product

    Attributes:
        name (str):
        amount (float | str):
        percentage (float | str):
    """

    name: str
    amount: float | str
    percentage: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        amount: float | str
        amount = self.amount

        percentage: float | str
        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "amount": amount,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        def _parse_percentage(data: object) -> float | str:
            return cast(float | str, data)

        percentage = _parse_percentage(d.pop("percentage"))

        product_cost_type_breakdown = cls(
            name=name,
            amount=amount,
            percentage=percentage,
        )

        product_cost_type_breakdown.additional_properties = d
        return product_cost_type_breakdown

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
