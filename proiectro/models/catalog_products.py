from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_product import CatalogProduct


T = TypeVar("T", bound="CatalogProducts")


@_attrs_define
class CatalogProducts:
    """
    Attributes:
        pricing_type (str):
        products (list[CatalogProduct]):
    """

    pricing_type: str
    products: list[CatalogProduct]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pricing_type = self.pricing_type

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pricing_type": pricing_type,
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_product import CatalogProduct

        d = dict(src_dict)
        pricing_type = d.pop("pricing_type")

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = CatalogProduct.from_dict(products_item_data)

            products.append(products_item)

        catalog_products = cls(
            pricing_type=pricing_type,
            products=products,
        )

        catalog_products.additional_properties = d
        return catalog_products

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
