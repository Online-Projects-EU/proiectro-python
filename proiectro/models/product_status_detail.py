from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductStatusDetail")


@_attrs_define
class ProductStatusDetail:
    """Product status for lifecycle display.
    Used in status dropdowns to show current status and all available lifecycle stages.
    Use lifecycle_type with templatetags for styling (status_bg, status_text, status_icon, etc.)

        Attributes:
            id (str):
            name (str):
            lifecycle_type (str):
            lifecycle_type_display (str):
            visible_to_customer (bool):
            sequence_no (int):
            is_current (bool):
    """

    id: str
    name: str
    lifecycle_type: str
    lifecycle_type_display: str
    visible_to_customer: bool
    sequence_no: int
    is_current: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        lifecycle_type = self.lifecycle_type

        lifecycle_type_display = self.lifecycle_type_display

        visible_to_customer = self.visible_to_customer

        sequence_no = self.sequence_no

        is_current = self.is_current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "lifecycle_type": lifecycle_type,
                "lifecycle_type_display": lifecycle_type_display,
                "visible_to_customer": visible_to_customer,
                "sequence_no": sequence_no,
                "is_current": is_current,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        lifecycle_type = d.pop("lifecycle_type")

        lifecycle_type_display = d.pop("lifecycle_type_display")

        visible_to_customer = d.pop("visible_to_customer")

        sequence_no = d.pop("sequence_no")

        is_current = d.pop("is_current")

        product_status_detail = cls(
            id=id,
            name=name,
            lifecycle_type=lifecycle_type,
            lifecycle_type_display=lifecycle_type_display,
            visible_to_customer=visible_to_customer,
            sequence_no=sequence_no,
            is_current=is_current,
        )

        product_status_detail.additional_properties = d
        return product_status_detail

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
