from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_operational_item_priority_type_0 import (
    EditOperationalItemPriorityType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditOperationalItem")


@_attrs_define
class EditOperationalItem:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        customer (None | str | Unset):
        customer_asset (None | str | Unset):
        priority (EditOperationalItemPriorityType0 | None | Unset):
        due_date (None | str | Unset):
        owner (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    customer: None | str | Unset = UNSET
    customer_asset: None | str | Unset = UNSET
    priority: EditOperationalItemPriorityType0 | None | Unset = UNSET
    due_date: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        customer: None | str | Unset
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        customer_asset: None | str | Unset
        if isinstance(self.customer_asset, Unset):
            customer_asset = UNSET
        else:
            customer_asset = self.customer_asset

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, EditOperationalItemPriorityType0):
            priority = self.priority.value
        else:
            priority = self.priority

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if customer is not UNSET:
            field_dict["customer"] = customer
        if customer_asset is not UNSET:
            field_dict["customer_asset"] = customer_asset
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_customer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer = _parse_customer(d.pop("customer", UNSET))

        def _parse_customer_asset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_asset = _parse_customer_asset(d.pop("customer_asset", UNSET))

        def _parse_priority(
            data: object,
        ) -> EditOperationalItemPriorityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = EditOperationalItemPriorityType0(data)

                return priority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditOperationalItemPriorityType0 | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        edit_operational_item = cls(
            name=name,
            description=description,
            customer=customer,
            customer_asset=customer_asset,
            priority=priority,
            due_date=due_date,
            owner=owner,
        )

        edit_operational_item.additional_properties = d
        return edit_operational_item

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
