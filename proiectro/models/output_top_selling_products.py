from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.top_selling_product import TopSellingProduct


T = TypeVar("T", bound="OutputTopSellingProducts")


@_attrs_define
class OutputTopSellingProducts:
    """Top selling products list

    Attributes:
        products (list[TopSellingProduct]):
        period (str):
    """

    products: list[TopSellingProduct]
    period: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_selling_product import TopSellingProduct

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = TopSellingProduct.from_dict(products_item_data)

            products.append(products_item)

        period = d.pop("period")

        output_top_selling_products = cls(
            products=products,
            period=period,
        )

        output_top_selling_products.additional_properties = d
        return output_top_selling_products

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
