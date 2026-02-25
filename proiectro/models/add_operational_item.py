from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_operational_item_priority import AddOperationalItemPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddOperationalItem")


@_attrs_define
class AddOperationalItem:
    """
    Attributes:
        process (str):
        name (str):
        description (str | Unset):  Default: ''.
        customer (None | str | Unset):
        priority (AddOperationalItemPriority | Unset):  Default: AddOperationalItemPriority.NORMAL.
        due_date (None | str | Unset):
    """

    process: str
    name: str
    description: str | Unset = ""
    customer: None | str | Unset = UNSET
    priority: AddOperationalItemPriority | Unset = AddOperationalItemPriority.NORMAL
    due_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process = self.process

        name = self.name

        description = self.description

        customer: None | str | Unset
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process": process,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if customer is not UNSET:
            field_dict["customer"] = customer
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process = d.pop("process")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        def _parse_customer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer = _parse_customer(d.pop("customer", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: AddOperationalItemPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = AddOperationalItemPriority(_priority)

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        add_operational_item = cls(
            process=process,
            name=name,
            description=description,
            customer=customer,
            priority=priority,
            due_date=due_date,
        )

        add_operational_item.additional_properties = d
        return add_operational_item

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
