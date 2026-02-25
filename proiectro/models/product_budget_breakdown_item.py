from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_cost_type_breakdown import ProductCostTypeBreakdown
    from ..models.product_status_detail import ProductStatusDetail


T = TypeVar("T", bound="ProductBudgetBreakdownItem")


@_attrs_define
class ProductBudgetBreakdownItem:
    """Product budget breakdown by cost type

    Attributes:
        product_id (str):
        product_name (str):
        product_url (str):
        current_status (ProductStatusDetail): Product status for lifecycle display.
            Used in status dropdowns to show current status and all available lifecycle stages.
            Use lifecycle_type with templatetags for styling (status_bg, status_text, status_icon, etc.)
        is_active (bool):
        cost_types (list[ProductCostTypeBreakdown]):
        total_cost (str):
    """

    product_id: str
    product_name: str
    product_url: str
    current_status: ProductStatusDetail
    is_active: bool
    cost_types: list[ProductCostTypeBreakdown]
    total_cost: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name

        product_url = self.product_url

        current_status = self.current_status.to_dict()

        is_active = self.is_active

        cost_types = []
        for cost_types_item_data in self.cost_types:
            cost_types_item = cost_types_item_data.to_dict()
            cost_types.append(cost_types_item)

        total_cost = self.total_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "product_name": product_name,
                "product_url": product_url,
                "current_status": current_status,
                "is_active": is_active,
                "cost_types": cost_types,
                "total_cost": total_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_cost_type_breakdown import ProductCostTypeBreakdown
        from ..models.product_status_detail import ProductStatusDetail

        d = dict(src_dict)
        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        product_url = d.pop("product_url")

        current_status = ProductStatusDetail.from_dict(d.pop("current_status"))

        is_active = d.pop("is_active")

        cost_types = []
        _cost_types = d.pop("cost_types")
        for cost_types_item_data in _cost_types:
            cost_types_item = ProductCostTypeBreakdown.from_dict(cost_types_item_data)

            cost_types.append(cost_types_item)

        total_cost = d.pop("total_cost")

        product_budget_breakdown_item = cls(
            product_id=product_id,
            product_name=product_name,
            product_url=product_url,
            current_status=current_status,
            is_active=is_active,
            cost_types=cost_types,
            total_cost=total_cost,
        )

        product_budget_breakdown_item.additional_properties = d
        return product_budget_breakdown_item

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
