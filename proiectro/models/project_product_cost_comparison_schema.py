from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_product_cost_comparison_product_schema import (
        ProjectProductCostComparisonProductSchema,
    )


T = TypeVar("T", bound="ProjectProductCostComparisonSchema")


@_attrs_define
class ProjectProductCostComparisonSchema:
    """Project product cost comparison data for grouped bar chart visualization

    The chart mode depends on financial management setting:
    - financial_mode=True: Shows grouped bars (proposal vs project cost)
    - simplified_mode=True: Shows single bars (proposal cost only)

        Attributes:
            project_id (str):
            project_name (str):
            products (list[ProjectProductCostComparisonProductSchema]):
            currency_symbol (str):
            max_cost (str):
            total_proposal_cost (str):
            total_project_cost (str):
            financial_mode (bool):
            simplified_mode (bool):
    """

    project_id: str
    project_name: str
    products: list[ProjectProductCostComparisonProductSchema]
    currency_symbol: str
    max_cost: str
    total_proposal_cost: str
    total_project_cost: str
    financial_mode: bool
    simplified_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        currency_symbol = self.currency_symbol

        max_cost = self.max_cost

        total_proposal_cost = self.total_proposal_cost

        total_project_cost = self.total_project_cost

        financial_mode = self.financial_mode

        simplified_mode = self.simplified_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "project_name": project_name,
                "products": products,
                "currency_symbol": currency_symbol,
                "max_cost": max_cost,
                "total_proposal_cost": total_proposal_cost,
                "total_project_cost": total_project_cost,
                "financial_mode": financial_mode,
                "simplified_mode": simplified_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_product_cost_comparison_product_schema import (
            ProjectProductCostComparisonProductSchema,
        )

        d = dict(src_dict)
        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ProjectProductCostComparisonProductSchema.from_dict(
                products_item_data
            )

            products.append(products_item)

        currency_symbol = d.pop("currency_symbol")

        max_cost = d.pop("max_cost")

        total_proposal_cost = d.pop("total_proposal_cost")

        total_project_cost = d.pop("total_project_cost")

        financial_mode = d.pop("financial_mode")

        simplified_mode = d.pop("simplified_mode")

        project_product_cost_comparison_schema = cls(
            project_id=project_id,
            project_name=project_name,
            products=products,
            currency_symbol=currency_symbol,
            max_cost=max_cost,
            total_proposal_cost=total_proposal_cost,
            total_project_cost=total_project_cost,
            financial_mode=financial_mode,
            simplified_mode=simplified_mode,
        )

        project_product_cost_comparison_schema.additional_properties = d
        return project_product_cost_comparison_schema

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
