from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_product import ProposalProduct


T = TypeVar("T", bound="ProposalProductSummary")


@_attrs_define
class ProposalProductSummary:
    """
    Attributes:
        total_value (float | str):
        total_cost (float | str):
        total_customer_price (float | str):
        total_profit (float | str):
        total_margin_amount (float | str):
        total_margin_percent (float | str):
        total_value_symbol (str):
        total_currency (str):
        product_count (int):
        active_product_count (int):
        total_items (int):
        avg_product_value (float | str):
        pricing_types_count (int):
        products_by_cost (list[ProposalProduct]):
        all_converted (bool):
        has_mixed_currencies (bool):
        warning_message (str):
    """

    total_value: float | str
    total_cost: float | str
    total_customer_price: float | str
    total_profit: float | str
    total_margin_amount: float | str
    total_margin_percent: float | str
    total_value_symbol: str
    total_currency: str
    product_count: int
    active_product_count: int
    total_items: int
    avg_product_value: float | str
    pricing_types_count: int
    products_by_cost: list[ProposalProduct]
    all_converted: bool
    has_mixed_currencies: bool
    warning_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_value: float | str
        total_value = self.total_value

        total_cost: float | str
        total_cost = self.total_cost

        total_customer_price: float | str
        total_customer_price = self.total_customer_price

        total_profit: float | str
        total_profit = self.total_profit

        total_margin_amount: float | str
        total_margin_amount = self.total_margin_amount

        total_margin_percent: float | str
        total_margin_percent = self.total_margin_percent

        total_value_symbol = self.total_value_symbol

        total_currency = self.total_currency

        product_count = self.product_count

        active_product_count = self.active_product_count

        total_items = self.total_items

        avg_product_value: float | str
        avg_product_value = self.avg_product_value

        pricing_types_count = self.pricing_types_count

        products_by_cost = []
        for products_by_cost_item_data in self.products_by_cost:
            products_by_cost_item = products_by_cost_item_data.to_dict()
            products_by_cost.append(products_by_cost_item)

        all_converted = self.all_converted

        has_mixed_currencies = self.has_mixed_currencies

        warning_message = self.warning_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_value": total_value,
                "total_cost": total_cost,
                "total_customer_price": total_customer_price,
                "total_profit": total_profit,
                "total_margin_amount": total_margin_amount,
                "total_margin_percent": total_margin_percent,
                "total_value_symbol": total_value_symbol,
                "total_currency": total_currency,
                "product_count": product_count,
                "active_product_count": active_product_count,
                "total_items": total_items,
                "avg_product_value": avg_product_value,
                "pricing_types_count": pricing_types_count,
                "products_by_cost": products_by_cost,
                "all_converted": all_converted,
                "has_mixed_currencies": has_mixed_currencies,
                "warning_message": warning_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_product import ProposalProduct

        d = dict(src_dict)

        def _parse_total_value(data: object) -> float | str:
            return cast(float | str, data)

        total_value = _parse_total_value(d.pop("total_value"))

        def _parse_total_cost(data: object) -> float | str:
            return cast(float | str, data)

        total_cost = _parse_total_cost(d.pop("total_cost"))

        def _parse_total_customer_price(data: object) -> float | str:
            return cast(float | str, data)

        total_customer_price = _parse_total_customer_price(
            d.pop("total_customer_price")
        )

        def _parse_total_profit(data: object) -> float | str:
            return cast(float | str, data)

        total_profit = _parse_total_profit(d.pop("total_profit"))

        def _parse_total_margin_amount(data: object) -> float | str:
            return cast(float | str, data)

        total_margin_amount = _parse_total_margin_amount(d.pop("total_margin_amount"))

        def _parse_total_margin_percent(data: object) -> float | str:
            return cast(float | str, data)

        total_margin_percent = _parse_total_margin_percent(
            d.pop("total_margin_percent")
        )

        total_value_symbol = d.pop("total_value_symbol")

        total_currency = d.pop("total_currency")

        product_count = d.pop("product_count")

        active_product_count = d.pop("active_product_count")

        total_items = d.pop("total_items")

        def _parse_avg_product_value(data: object) -> float | str:
            return cast(float | str, data)

        avg_product_value = _parse_avg_product_value(d.pop("avg_product_value"))

        pricing_types_count = d.pop("pricing_types_count")

        products_by_cost = []
        _products_by_cost = d.pop("products_by_cost")
        for products_by_cost_item_data in _products_by_cost:
            products_by_cost_item = ProposalProduct.from_dict(
                products_by_cost_item_data
            )

            products_by_cost.append(products_by_cost_item)

        all_converted = d.pop("all_converted")

        has_mixed_currencies = d.pop("has_mixed_currencies")

        warning_message = d.pop("warning_message")

        proposal_product_summary = cls(
            total_value=total_value,
            total_cost=total_cost,
            total_customer_price=total_customer_price,
            total_profit=total_profit,
            total_margin_amount=total_margin_amount,
            total_margin_percent=total_margin_percent,
            total_value_symbol=total_value_symbol,
            total_currency=total_currency,
            product_count=product_count,
            active_product_count=active_product_count,
            total_items=total_items,
            avg_product_value=avg_product_value,
            pricing_types_count=pricing_types_count,
            products_by_cost=products_by_cost,
            all_converted=all_converted,
            has_mixed_currencies=has_mixed_currencies,
            warning_message=warning_message,
        )

        proposal_product_summary.additional_properties = d
        return proposal_product_summary

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
