from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TopSellingProduct")


@_attrs_define
class TopSellingProduct:
    """Individual top selling product

    Attributes:
        rank (int):
        product_id (str):
        product_name (str):
        product_type (str):
        product_type_display (str):
        units_sold (int):
        total_revenue (float | str):
        currency_symbol (str):
    """

    rank: int
    product_id: str
    product_name: str
    product_type: str
    product_type_display: str
    units_sold: int
    total_revenue: float | str
    currency_symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        product_id = self.product_id

        product_name = self.product_name

        product_type = self.product_type

        product_type_display = self.product_type_display

        units_sold = self.units_sold

        total_revenue: float | str
        total_revenue = self.total_revenue

        currency_symbol = self.currency_symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "product_id": product_id,
                "product_name": product_name,
                "product_type": product_type,
                "product_type_display": product_type_display,
                "units_sold": units_sold,
                "total_revenue": total_revenue,
                "currency_symbol": currency_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rank = d.pop("rank")

        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        product_type = d.pop("product_type")

        product_type_display = d.pop("product_type_display")

        units_sold = d.pop("units_sold")

        def _parse_total_revenue(data: object) -> float | str:
            return cast(float | str, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue"))

        currency_symbol = d.pop("currency_symbol")

        top_selling_product = cls(
            rank=rank,
            product_id=product_id,
            product_name=product_name,
            product_type=product_type,
            product_type_display=product_type_display,
            units_sold=units_sold,
            total_revenue=total_revenue,
            currency_symbol=currency_symbol,
        )

        top_selling_product.additional_properties = d
        return top_selling_product

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
