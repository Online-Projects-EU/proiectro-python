from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddCustomerLocation")


@_attrs_define
class AddCustomerLocation:
    """
    Attributes:
        customer (str):
        location (str):
        name (str):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        is_active (bool | Unset):  Default: False.
    """

    customer: str
    location: str
    name: str
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    is_active: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer = self.customer

        location = self.location

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "location": location,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer = d.pop("customer")

        location = d.pop("location")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        is_active = d.pop("is_active", UNSET)

        add_customer_location = cls(
            customer=customer,
            location=location,
            name=name,
            description=description,
            internal_code=internal_code,
            is_active=is_active,
        )

        add_customer_location.additional_properties = d
        return add_customer_location

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
