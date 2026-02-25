from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductStatusTransition")


@_attrs_define
class ProductStatusTransition:
    """A status transition option for the product menu

    Attributes:
        status_id (int):
        name (str):
        lifecycle_type (str):
    """

    status_id: int
    name: str
    lifecycle_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_id = self.status_id

        name = self.name

        lifecycle_type = self.lifecycle_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_id": status_id,
                "name": name,
                "lifecycle_type": lifecycle_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_id = d.pop("status_id")

        name = d.pop("name")

        lifecycle_type = d.pop("lifecycle_type")

        product_status_transition = cls(
            status_id=status_id,
            name=name,
            lifecycle_type=lifecycle_type,
        )

        product_status_transition.additional_properties = d
        return product_status_transition

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
