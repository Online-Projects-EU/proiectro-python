from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linked_product import LinkedProduct


T = TypeVar("T", bound="TemplateLinkedProducts")


@_attrs_define
class TemplateLinkedProducts:
    """Catalog products linked to a specific work item template

    Attributes:
        template_id (str):
        template_name (str):
        linked_products (list[LinkedProduct]):
    """

    template_id: str
    template_name: str
    linked_products: list[LinkedProduct]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        template_name = self.template_name

        linked_products = []
        for linked_products_item_data in self.linked_products:
            linked_products_item = linked_products_item_data.to_dict()
            linked_products.append(linked_products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "template_name": template_name,
                "linked_products": linked_products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_product import LinkedProduct

        d = dict(src_dict)
        template_id = d.pop("template_id")

        template_name = d.pop("template_name")

        linked_products = []
        _linked_products = d.pop("linked_products")
        for linked_products_item_data in _linked_products:
            linked_products_item = LinkedProduct.from_dict(linked_products_item_data)

            linked_products.append(linked_products_item)

        template_linked_products = cls(
            template_id=template_id,
            template_name=template_name,
            linked_products=linked_products,
        )

        template_linked_products.additional_properties = d
        return template_linked_products

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
