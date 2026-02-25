from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_status_transition import ProductStatusTransition


T = TypeVar("T", bound="ProductMenuItems")


@_attrs_define
class ProductMenuItems:
    """Product menu items for dynamic updates

    Attributes:
        product_id (str):
        is_active (bool):
        status_transitions (list[ProductStatusTransition] | Unset):
        lifecycle_name (None | str | Unset):
        current_status_name (None | str | Unset):
    """

    product_id: str
    is_active: bool
    status_transitions: list[ProductStatusTransition] | Unset = UNSET
    lifecycle_name: None | str | Unset = UNSET
    current_status_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        is_active = self.is_active

        status_transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_transitions, Unset):
            status_transitions = []
            for status_transitions_item_data in self.status_transitions:
                status_transitions_item = status_transitions_item_data.to_dict()
                status_transitions.append(status_transitions_item)

        lifecycle_name: None | str | Unset
        if isinstance(self.lifecycle_name, Unset):
            lifecycle_name = UNSET
        else:
            lifecycle_name = self.lifecycle_name

        current_status_name: None | str | Unset
        if isinstance(self.current_status_name, Unset):
            current_status_name = UNSET
        else:
            current_status_name = self.current_status_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "is_active": is_active,
            }
        )
        if status_transitions is not UNSET:
            field_dict["status_transitions"] = status_transitions
        if lifecycle_name is not UNSET:
            field_dict["lifecycle_name"] = lifecycle_name
        if current_status_name is not UNSET:
            field_dict["current_status_name"] = current_status_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_status_transition import ProductStatusTransition

        d = dict(src_dict)
        product_id = d.pop("product_id")

        is_active = d.pop("is_active")

        _status_transitions = d.pop("status_transitions", UNSET)
        status_transitions: list[ProductStatusTransition] | Unset = UNSET
        if _status_transitions is not UNSET:
            status_transitions = []
            for status_transitions_item_data in _status_transitions:
                status_transitions_item = ProductStatusTransition.from_dict(
                    status_transitions_item_data
                )

                status_transitions.append(status_transitions_item)

        def _parse_lifecycle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_name = _parse_lifecycle_name(d.pop("lifecycle_name", UNSET))

        def _parse_current_status_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_status_name = _parse_current_status_name(
            d.pop("current_status_name", UNSET)
        )

        product_menu_items = cls(
            product_id=product_id,
            is_active=is_active,
            status_transitions=status_transitions,
            lifecycle_name=lifecycle_name,
            current_status_name=current_status_name,
        )

        product_menu_items.additional_properties = d
        return product_menu_items

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
