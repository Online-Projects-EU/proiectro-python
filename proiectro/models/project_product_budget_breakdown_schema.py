from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_budget_breakdown_item import ProductBudgetBreakdownItem


T = TypeVar("T", bound="ProjectProductBudgetBreakdownSchema")


@_attrs_define
class ProjectProductBudgetBreakdownSchema:
    """Project product budget breakdown showing cost type composition

    Only returns detailed breakdown if financial management is enabled:
    - financial_mode=True: Shows cost breakdowns with pie charts
    - simplified_mode=True: Returns empty list (no breakdown displayed)

        Attributes:
            products (list[ProductBudgetBreakdownItem]):
            currency_symbol (str):
            financial_mode (bool):
            simplified_mode (bool):
    """

    products: list[ProductBudgetBreakdownItem]
    currency_symbol: str
    financial_mode: bool
    simplified_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        currency_symbol = self.currency_symbol

        financial_mode = self.financial_mode

        simplified_mode = self.simplified_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "currency_symbol": currency_symbol,
                "financial_mode": financial_mode,
                "simplified_mode": simplified_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_budget_breakdown_item import ProductBudgetBreakdownItem

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ProductBudgetBreakdownItem.from_dict(products_item_data)

            products.append(products_item)

        currency_symbol = d.pop("currency_symbol")

        financial_mode = d.pop("financial_mode")

        simplified_mode = d.pop("simplified_mode")

        project_product_budget_breakdown_schema = cls(
            products=products,
            currency_symbol=currency_symbol,
            financial_mode=financial_mode,
            simplified_mode=simplified_mode,
        )

        project_product_budget_breakdown_schema.additional_properties = d
        return project_product_budget_breakdown_schema

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
