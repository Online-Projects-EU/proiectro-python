from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_work_item import ProductWorkItem


T = TypeVar("T", bound="ProductWorkItems")


@_attrs_define
class ProductWorkItems:
    """List of work items linked to a product in a project

    Attributes:
        product_id (str):
        product_name (str):
        project_id (str):
        project_name (str):
        work_items (list[ProductWorkItem]):
        total (int):
    """

    product_id: str
    product_name: str
    project_id: str
    project_name: str
    work_items: list[ProductWorkItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name

        project_id = self.project_id

        project_name = self.project_name

        work_items = []
        for work_items_item_data in self.work_items:
            work_items_item = work_items_item_data.to_dict()
            work_items.append(work_items_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "product_name": product_name,
                "project_id": project_id,
                "project_name": project_name,
                "work_items": work_items,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_work_item import ProductWorkItem

        d = dict(src_dict)
        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        work_items = []
        _work_items = d.pop("work_items")
        for work_items_item_data in _work_items:
            work_items_item = ProductWorkItem.from_dict(work_items_item_data)

            work_items.append(work_items_item)

        total = d.pop("total")

        product_work_items = cls(
            product_id=product_id,
            product_name=product_name,
            project_id=project_id,
            project_name=project_name,
            work_items=work_items,
            total=total,
        )

        product_work_items.additional_properties = d
        return product_work_items

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
