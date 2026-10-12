from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        currency_symbol (str):
        total_revenue (float | None | str | Unset):
        currency_code (str | Unset):  Default: ''.
    """

    rank: int
    product_id: str
    product_name: str
    product_type: str
    product_type_display: str
    units_sold: int
    currency_symbol: str
    total_revenue: float | None | str | Unset = UNSET
    currency_code: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        product_id = self.product_id

        product_name = self.product_name

        product_type = self.product_type

        product_type_display = self.product_type_display

        units_sold = self.units_sold

        currency_symbol = self.currency_symbol

        total_revenue: float | None | str | Unset
        if isinstance(self.total_revenue, Unset):
            total_revenue = UNSET
        else:
            total_revenue = self.total_revenue

        currency_code = self.currency_code

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
                "currency_symbol": currency_symbol,
            }
        )
        if total_revenue is not UNSET:
            field_dict["total_revenue"] = total_revenue
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code

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

        currency_symbol = d.pop("currency_symbol")

        def _parse_total_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue", UNSET))

        currency_code = d.pop("currency_code", UNSET)

        top_selling_product = cls(
            rank=rank,
            product_id=product_id,
            product_name=product_name,
            product_type=product_type,
            product_type_display=product_type_display,
            units_sold=units_sold,
            currency_symbol=currency_symbol,
            total_revenue=total_revenue,
            currency_code=currency_code,
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
