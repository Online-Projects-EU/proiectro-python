from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_resource_usage_item import ProductResourceUsageItem


T = TypeVar("T", bound="ProductResourceUsagesOutput")


@_attrs_define
class ProductResourceUsagesOutput:
    """Resource usages for work items linked to a product

    Attributes:
        resource_usage (list[ProductResourceUsageItem]):
        total_usage (int):
        usage_count (int):
        project_id (str):
        project_name (str):
        product_id (str):
        product_name (str):
    """

    resource_usage: list[ProductResourceUsageItem]
    total_usage: int
    usage_count: int
    project_id: str
    project_name: str
    product_id: str
    product_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_usage = []
        for resource_usage_item_data in self.resource_usage:
            resource_usage_item = resource_usage_item_data.to_dict()
            resource_usage.append(resource_usage_item)

        total_usage = self.total_usage

        usage_count = self.usage_count

        project_id = self.project_id

        project_name = self.project_name

        product_id = self.product_id

        product_name = self.product_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_usage": resource_usage,
                "total_usage": total_usage,
                "usage_count": usage_count,
                "project_id": project_id,
                "project_name": project_name,
                "product_id": product_id,
                "product_name": product_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_resource_usage_item import ProductResourceUsageItem

        d = dict(src_dict)
        resource_usage = []
        _resource_usage = d.pop("resource_usage")
        for resource_usage_item_data in _resource_usage:
            resource_usage_item = ProductResourceUsageItem.from_dict(
                resource_usage_item_data
            )

            resource_usage.append(resource_usage_item)

        total_usage = d.pop("total_usage")

        usage_count = d.pop("usage_count")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        product_resource_usages_output = cls(
            resource_usage=resource_usage,
            total_usage=total_usage,
            usage_count=usage_count,
            project_id=project_id,
            project_name=project_name,
            product_id=product_id,
            product_name=product_name,
        )

        product_resource_usages_output.additional_properties = d
        return product_resource_usages_output

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
