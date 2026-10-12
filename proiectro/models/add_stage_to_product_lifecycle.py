from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddStageToProductLifecycle")


@_attrs_define
class AddStageToProductLifecycle:
    """
    Attributes:
        sequence_no (int):
        name (str):
        lifecycle_type (str):
        visible_to_customer (bool | None | Unset):  Default: False.
        is_active (bool | None | Unset):  Default: False.
    """

    sequence_no: int
    name: str
    lifecycle_type: str
    visible_to_customer: bool | None | Unset = False
    is_active: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sequence_no = self.sequence_no

        name = self.name

        lifecycle_type = self.lifecycle_type

        visible_to_customer: bool | None | Unset
        if isinstance(self.visible_to_customer, Unset):
            visible_to_customer = UNSET
        else:
            visible_to_customer = self.visible_to_customer

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sequence_no": sequence_no,
                "name": name,
                "lifecycle_type": lifecycle_type,
            }
        )
        if visible_to_customer is not UNSET:
            field_dict["visible_to_customer"] = visible_to_customer
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sequence_no = d.pop("sequence_no")

        name = d.pop("name")

        lifecycle_type = d.pop("lifecycle_type")

        def _parse_visible_to_customer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible_to_customer = _parse_visible_to_customer(
            d.pop("visible_to_customer", UNSET)
        )

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        add_stage_to_product_lifecycle = cls(
            sequence_no=sequence_no,
            name=name,
            lifecycle_type=lifecycle_type,
            visible_to_customer=visible_to_customer,
            is_active=is_active,
        )

        add_stage_to_product_lifecycle.additional_properties = d
        return add_stage_to_product_lifecycle

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
