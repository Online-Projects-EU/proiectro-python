from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TenantProductLifecycle")


@_attrs_define
class TenantProductLifecycle:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        is_default (bool):
        is_active (bool):
        sequence_no (int):
    """

    id: str
    name: str
    description: str
    is_default: bool
    is_active: bool
    sequence_no: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_default = self.is_default

        is_active = self.is_active

        sequence_no = self.sequence_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_default": is_default,
                "is_active": is_active,
                "sequence_no": sequence_no,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_default = d.pop("is_default")

        is_active = d.pop("is_active")

        sequence_no = d.pop("sequence_no")

        tenant_product_lifecycle = cls(
            id=id,
            name=name,
            description=description,
            is_default=is_default,
            is_active=is_active,
            sequence_no=sequence_no,
        )

        tenant_product_lifecycle.additional_properties = d
        return tenant_product_lifecycle

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
